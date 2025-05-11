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
  - Python 3.13+
- **Dependencies**:
  - streamlit>=1.45.0
  - streamlit-extras>=0.7.1
  - langgraph>=0.4.3
  - langchain[anthropic,google-genai,google-vertexai]>=0.3.25
  - python-dotenv>=1.1.0
  - ipykernel>=6.29.5

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd <repository-name>
   ```

2. **Install uv (if not already installed)**
   ```bash
   pip install uv
   ```

3. **Install dependencies using uv**
   ```bash
   uv pip install -e .
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run frontend.py
   ```

## 📁 Project Structure

- `frontend.py`: Streamlit UI implementation with custom styling
- `backend.py`: Core logic for message processing and response generation
- `simple_chatbot.py`: Basic implementation example
- `pyproject.toml`: Project configuration and dependencies

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