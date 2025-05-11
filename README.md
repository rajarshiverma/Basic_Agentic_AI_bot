# 🤖 AI Assistant - Emotional & Logical Companion

A sophisticated AI chatbot application that provides both emotional support and logical assistance using Streamlit for the frontend and LangGraph for the backend processing.

## ✨ Features

- **Dual-Mode Responses**: Intelligently classifies user queries and responds with either:
  - 🤗 Emotional support (therapist mode)
  - 🧠 Logical analysis (assistant mode)
- **Beautiful UI**: 
  - Animated rainbow borders
  - Modern chat interface
  - Responsive message bubbles
  - Custom styling and animations
- **Smart Processing**:
  - Message classification using Gemini 2.0
  - State management with LangGraph
  - Real-time typing effect
  - Markdown support in responses

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: 
  - LangGraph for workflow management
  - Google's Gemini 2.0 Flash model
  - Python 3.x
- **Dependencies**:
  - streamlit
  - streamlit-extras
  - langgraph
  - langchain
  - python-dotenv
  - google-generativeai

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd <repository-name>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run frontend.py
   ```

## 📁 Project Structure

- `frontend.py`: Streamlit UI implementation with custom styling
- `backend.py`: Core logic for message processing and response generation
- `simple_chatbot.py`: Basic implementation example

## 🔄 How It Works

1. User sends a message through the Streamlit interface
2. The message is processed by the LangGraph workflow:
   - Message classification (emotional vs logical)
   - Routing to appropriate response agent
   - Response generation
3. The response is displayed with a typing effect in the chat interface

## 🎨 UI Features

- Animated rainbow borders for input fields
- Custom-styled message bubbles
- Gradient text effects
- Responsive layout
- Emoji support
- Markdown rendering

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini for the AI model
- Streamlit for the web framework
- LangGraph for workflow management