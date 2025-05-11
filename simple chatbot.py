from dotenv import load_dotenv
from typing import Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict

load_dotenv()

llm = init_chat_model(
    "gemini-2.0-flash",
    model_provider="google_genai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def chatbot(state: State):
    # Get the AI response (returns AIMessage)
    ai_message = llm.invoke(state["messages"])
    # Return in a format that matches the State structure
    return {"messages": [ai_message]}  # Keep as AIMessage (LangGraph handles it)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(start_key=START, end_key="chatbot")
graph_builder.add_edge(start_key="chatbot", end_key=END)

graph = graph_builder.compile()

user_input = input("Enter a message: ") 
state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})

# Extract content from the last AIMessage in the list
last_message = state["messages"][-1]
print(last_message.content)  # Correctly access AIMessage's content