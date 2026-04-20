# YouTube Content Creation Agent

This project is a YouTube Content Creation Agent that helps generate video scripts based on real-time information.

## Prerequisites

- Python 3.13 or higher
- uv package manager (install from https://github.com/astral-sh/uv)

## Setup

1. Clone the repository and navigate to the project directory.

2. Install dependencies using uv:
   ```
   uv sync
   ```

3. Create a `.env` file in the root directory and add your API keys:
   ```
   GEMINI_API_KEY=your_google_generative_ai_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

## How to Run

### Option 1: Run as MCP Server

To run the project as an MCP (Model Context Protocol) server:

```
uv run mcp dev mcp_server.py
```

This starts the MCP server with tools for getting real-time information and generating video scripts.

### Option 2: Run Flask Web App

To run the web demo using Flask:

```
uv run python flask_app.py
```

Then open your browser to `http://localhost:5000` (or the port specified in the app).

### Option 3: Run Streamlit Demo

To run the Streamlit demo:

```
uv run streamlit run demo.py
```

This launches the Streamlit app in your browser.

## Project Structure

- `mcp_server.py`: MCP server implementation
- `flask_app.py`: Flask web application
- `demo.py`: Streamlit demo app
- `app.py`: Core logic for information retrieval and script generation
- `all-utils/`: Utility modules and examples





mcp install mcp_server.py 


uv run mcp dev mcp_server.py
