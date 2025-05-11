from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

load_dotenv()

llm = init_chat_model(
    "gemini-2.0-flash",
    model_provider="google_genai"
)

class MessageClassifier(BaseModel):
    message_type: Literal["emotional", "logical"] = Field(
        ...,
        description="Classify if the message requires an emotional(therapist) or logical(assistant) response",
    )

class State(TypedDict):
    messages: Annotated[list, add_messages]
    message_type: str | None
    next: str | None

graph_builder = StateGraph(State)

def classify_message(state: State):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)
    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """Classify the user message as either:
            - 'emotional': if emotional support/therapy needed
            - 'logical': if factual information needed"""
        },
        {"role":"user", "content": last_message.content}
    ])
    return {"message_type": result.message_type}

def router(state: State):
    message_type = state.get("message_type", "logical")
    return {"next": "therapist"} if message_type == "emotional" else {"next": "logical"}
    
def therapist_agent(state: State):
    last_message = state["messages"][-1]
    reply = llm.invoke([
        {
            "role": "system",
            "content": "You are a compassionate therapist. Provide emotional support."
        },
        {"role": "user", "content": last_message.content}
    ])
    return {"messages": [{"role": "assistant", "content": reply.content}]}

def logical_agent(state: State):
    last_message = state["messages"][-1]
    reply = llm.invoke([
        {
            "role": "system",
            "content": "You are a logical assistant. Provide factual information."
        },
        {"role": "user", "content": last_message.content}
    ])
    return {"messages": [{"role": "assistant", "content": reply.content}]}

# Build graph
graph_builder.add_node("classifier", classify_message)
graph_builder.add_node("router", router)
graph_builder.add_node("therapist", therapist_agent)
graph_builder.add_node("logical", logical_agent)

graph_builder.add_edge(START, "classifier")
graph_builder.add_edge("classifier", "router")
graph_builder.add_conditional_edges(
    "router",
    lambda state: state.get("next"),
    {"therapist": "therapist", "logical": "logical"}
)
graph_builder.add_edge("therapist", END)
graph_builder.add_edge("logical", END)

graph = graph_builder.compile()

def process_message(user_input: str, chat_history=None):
    state = {
        "messages": [{"role": "user", "content": user_input}],
        "message_type": None,
        "next": None
    }
    if chat_history:
        state["messages"] = chat_history + state["messages"]
    
    state = graph.invoke(state)
    return state["messages"][-1].content  # Directly return the content string
# if __name__ == "__main__":
#     run_chatbot()


# -------------------------------------------------------------
# Snippet to get the graph visualization this can be done in jupyter notebook
# from IPython.display import Image, display

# try:
#     display(Image(graph.get_graph().draw_mermaid_png()))
# except Exception:
#     pass
# -------------------------------------------------------------