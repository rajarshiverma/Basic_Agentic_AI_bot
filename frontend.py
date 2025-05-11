import streamlit as st
from backend import graph, process_message
import time

# Setup
st.set_page_config(page_title="AI Assistant", layout="centered")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)
    
    # Get and display assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Thinking..."):
            # Process message through original backend
            response = process_message(
                prompt,
                st.session_state.messages[:-1]  # Pass history
            )
            
            # Typewriter effect
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)
        
        # Add to history
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )