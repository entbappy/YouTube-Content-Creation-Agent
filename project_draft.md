# YouTube Content Creation StoryForge Agent

StoryForge Agent is a cutting-edge, Streamlit-based application designed to streamline the research and content creation process for video creators. By combining real-time search capabilities with advanced large language models (LLMs), it allows users to go from a simple topic query to a polished short-form video script in seconds.

## 🚀 Key Features

- **Real-Time Research**: Leverages the **Tavily Search API** to fetch the latest news, trends, and factual information on any given topic.
- **AI-Powered Summarization**: Uses **Google's Gemini 2.0 Flash** to distill raw search results into concise, engaging, and professional summaries.
- **Script Generation**: Automatically transforms researched insights into high-impact scripts optimized for **YouTube Shorts** or **Instagram Reels**.
- **Interactive UI**: A modern, responsive Streamlit dashboard featuring glassmorphism aesthetics and smooth transitions.
- **MCP Integration**: Includes a **Model Context Protocol (MCP)** server for seamless integration with AI agents and other developer ecosystems.

## 🛠️ Tech Stack

- **Framework**: [Streamlit](https://streamlit.io/) (Web UI)
- **AI Models**: [Google Gemini 2.0 Flash](https://aistudio.google.com/) (Summarization & Scripting)
- **Search API**: [Tavily](https://tavily.com/) (Real-time data retrieval)
- **Programming Language**: Python
- **Package Management**: [uv](https://github.com/astral-sh/uv)
- **Messaging/Protocols**: Model Context Protocol (MCP)

## 🏗️ Architecture Overview

The application follows a modular architecture:
1.  **Frontend (app.py)**: Manages the Streamlit user interface, handling user inputs, displaying AI-generated cards, and providing download capabilities.
2.  **Core Logic (app.py)**: Houses functions like `get_realtime_info` and `generate_video_script` that communicate with external APIs (Tavily and Gemini).
3.  **MCP Layer (mcp_server.py)**: Exposes the core logic as tools natively compatible with the FastMCP framework, allowing AI agents to call these research and scripting functions.

## ⚙️ Setup and Installation

### Prerequisites
- Python installed (recommended via `uv`)
- API keys for **Google Gemini** and **Tavily**

### Installation Steps

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd "YouTube Content Creation StoryForge Agent"
    ```

2.  **Configure Environment Variables**:
    Create a `.env` file in the root directory and add your keys:
    ```env
    GEMINI_API_KEY=your_gemini_key_here
    TAVILY_API_KEY=your_tavily_key_here
    ```

3.  **Run the Application**:
    Using `uv`:
    ```bash
    uv run streamlit run app.py
    ```

## 🤖 MCP Server Usage

You can also use this project as an MCP server to provide research and scripting tools to your AI agent.

- **To run in dev mode**:
  ```bash
  uv run mcp dev mcp_server.py
  ```
- **To install as a tool**:
  ```bash
  mcp install mcp_server.py
  ```

## 📋 Project Metadata

### 1. Learning Outcome:
   - Master building AI-powered content creation pipelines using Google Gemini and real-time search APIs.
   - Implement a modern web interface using Streamlit with custom CSS theming and glassmorphism design.
   - Understand how to integrate the Tavily Search API for real-time web data retrieval and summarization.
   - Gain hands-on experience with Google's Gemini 2.0 Flash model for text summarization and creative script writing.
   - Learn to expose application logic as tools via the Model Context Protocol (MCP) using FastMCP.
   - Develop environment-driven configuration management using Python-dotenv.

### 2. What You Will Build:
   - A "YouTube Content Creation StoryForge Agent" capable of researching any topic and generating short-form video scripts.
   - A real-time research pipeline that fetches the latest information from the web and summarizes it using an LLM.
   - A Streamlit-based web dashboard with a premium dark-themed UI for interactive content creation.
   - An MCP server that exposes research and scripting tools for integration with AI agents like Claude Desktop.
   - A downloadable script generator optimized for YouTube Shorts and Instagram Reels.

### 3. Prerequisite:
   - Proficiency in Python programming.
   - Basic understanding of working with APIs (REST APIs, API keys).
   - Familiarity with Streamlit or any Python web framework.
   - A Google Gemini API key and a Tavily API key.
   - Basic knowledge of Large Language Models (LLMs) and prompt engineering.

### 4. Technologies:
   - Programming Language: Python
   - Web Framework: Streamlit
   - LLM Provider: Google Gemini 2.0 Flash
   - Search API: Tavily
   - Protocol: Model Context Protocol (MCP) via FastMCP
   - Package Management: uv
   - Environment Management: Python-dotenv
   - Frontend Styling: Custom CSS (Glassmorphism, Gradients)

---
*Developed with Passion for Creators.*
