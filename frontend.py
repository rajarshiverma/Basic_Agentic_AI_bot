import streamlit as st
from backend import process_message
import time
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain

# Custom CSS for rainbow border and text formatting
st.markdown("""
    <style>
    @keyframes rotate-gradient {
        0% {
            border-image: linear-gradient(0deg, #ff0000, #ff8000, #ffff00, #00ff00, #0000ff, #8000ff) 1;
        }
        120% {
            border-image: linear-gradient(360deg, #ff0000, #ff8000, #ffff00, #00ff00, #0000ff, #8000ff) 1;
        }
    }
    
    /* Animated rainbow border for text input */
    .stChatInput {
        border: 3px solid;
        border-image: linear-gradient(0deg, #ff0000, #ff8000, #ffff00, #00ff00, #0000ff, #8000ff) 1;
        border-radius: 20px;
        padding: 10px;
        margin-top: 20px;
        animation: rotate-gradient 4s linear infinite;
    }
    
    /* Better message bubbles */
    .stChatMessage {
        border-radius: 15px !important;
        padding: 15px !important;
        margin: 10px 0 !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1) !important;
    }
    
    /* User message bubble */
    [data-testid="stChatMessage"]:has(div:contains("user")) {
        background-color: #f0f8ff !important;
        border-left: 5px solid #4e8cff !important;
    }
    
    /* Assistant message bubble */
    [data-testid="stChatMessage"]:has(div:contains("assistant")) {
        background-color: #f5f5f5 !important;
        border-left: 5px solid #ff6b6b !important;
    }
    
    /* Better text formatting */
    .markdown-text-container p {
        line-height: 1.6 !important;
        margin-bottom: 12px !important;
    }
    
    /* Header styling */
    .header {
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin-bottom: 30px;
    }
    
    .title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #ff0000, #ff8000, #ffff00, #00ff00, #0000ff, #8000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# Fun animation on first load
if "animation_done" not in st.session_state:
    rain(
        emoji="✨",
        font_size=30,
        falling_speed=5,
        animation_length=1,
    )
    st.session_state.animation_done = True

# App Header
st.markdown("""
    <div class="header">
        <div class="title">🤖 AI Assistant</div>
        <div class="subtitle">Your emotional & logical companion</div>
    </div>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI assistant. How can I help you today? 😊\n\nI can provide:\n- 🤗 Emotional support\n- 🧠 Logical analysis\n\nJust start typing below!"}
    ]

# Display chat messages with better formatting
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        # We'll use st.markdown directly for the content to properly render Markdown
        st.markdown(msg["content"])

# Chat input with rainbow border
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with typing effect
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Thinking..."):
            assistant_response = process_message(
                prompt,
                st.session_state.messages[:-1]
            )
        
        # Split response into chunks by newlines while preserving Markdown
        chunks = assistant_response.split('\n')
        
        # Simulate typing with proper Markdown rendering
        for chunk in chunks:
            if chunk.strip():  # Only add non-empty chunks
                full_response += chunk + "\n"
                message_placeholder.markdown(full_response)
                time.sleep(0.1)
        
        # Final message with Markdown formatting
        message_placeholder.markdown(assistant_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})