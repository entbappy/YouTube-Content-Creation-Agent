# YouTube Content Creation Agent

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![UV](https://img.shields.io/badge/package%20manager-uv-orange.svg)](https://github.com/astral-sh/uv)

An intelligent AI-powered agent for creating YouTube video content, including script generation, real-time information retrieval, and content optimization using advanced language models and web search capabilities.

## 🌟 Features

- **Real-time Information Retrieval**: Integrates with Tavily API for up-to-date web search and data gathering
- **AI-Powered Script Generation**: Uses Google's Gemini 2.0 Flash model for high-quality video script creation
- **Multiple Interface Options**: 
  - MCP (Model Context Protocol) server for integration with AI assistants
  - Flask web application for web-based interaction
  - Streamlit demo app for quick testing
- **Modular Architecture**: Clean separation of concerns with utility modules for logging, validation, and memory management
- **Fast Setup**: Optional UV package manager for lightning-fast dependency installation

## 🏗️ Architecture Overview

![Project Architecture](Assets/3242%20(1).png)

The system consists of multiple components working together to generate YouTube content:

- **MCP Server**: Provides tools for AI assistants to interact with the content creation pipeline
- **Flask Web App**: User-friendly web interface for content generation
- **Streamlit Demo**: Quick demonstration interface
- **Core Logic**: Handles information retrieval and script generation
- **Utilities**: Supporting modules for validation, logging, and memory management

## 📋 Prerequisites

- Python 3.13 or higher
- API Keys for:
  - Google Generative AI (Gemini)
  - Tavily (Web search)

## 🚀 Installation

### Option 1: Standard Installation (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd youtube-content-creation-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: UV Package Manager (Faster Setup)

For a much faster installation experience, use the [UV package manager](https://github.com/astral-sh/uv):

1. **Install UV** (if not already installed)
   ```bash
   # On Windows
   winget install astral-sh.uv
   # Or using pip
   pip install uv
   ```

2. **Clone and setup**
   ```bash
   git clone <repository-url>
   cd youtube-content-creation-agent
   uv sync
   ```

## ⚙️ Configuration

Create a `.env` file in the root directory with your API keys:

```env
GEMINI_API_KEY=your_google_generative_ai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## 🎯 Usage

### MCP Server Mode

Run as an MCP server for integration with AI assistants:

```bash
# Using UV
uv run mcp dev mcp_server.py

# Or with standard Python
python mcp_server.py
```

### Flask Web Application

Launch the web interface:

```bash
# Using UV
uv run python flask_app.py

# Or with standard Python
python flask_app.py
```

Open your browser to `http://localhost:5000` to access the web app.

### Streamlit Demo

Run the interactive demo:

```bash
# Using UV
uv run streamlit run demo.py

# Or with standard Python
streamlit run demo.py
```

## 📁 Project Structure

```
youtube-content-creation-agent/
├── app.py                 # Core application logic
├── flask_app.py           # Flask web application
├── demo.py                # Streamlit demo interface
├── mcp_server.py         # MCP server implementation
├── main.py                # Main entry point
├── pyproject.toml         # Project configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── Assets/                # Project assets and screenshots
│   └── 3242 (1).png      # Architecture diagram
├── all-utils/             # Utility modules
│   ├── main.py
│   ├── requirements.txt
│   ├── db/               # Database files
│   └── utilities/        # Utility scripts and notebooks
│       ├── pydantic_models.py
│       ├── query_validation_transformation.py
│       ├── logging_example.py
│       └── mem0_example.py
└── docs/                 # Documentation (see docs/ folder)
```

## 📚 Documentation

Detailed documentation is available in the [`docs/`](docs/) folder:

- [Installation Guide](docs/installation.md)
- [Usage Examples](docs/usage.md)
- [API Reference](docs/api.md)
- [Contributing](docs/contributing.md)

## 🔄 Workflows

Visual workflow diagrams for all components are available in the [`workflows/`](workflows/) folder.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Generative AI for the Gemini model
- Tavily for web search capabilities
- Streamlit and Flask for UI frameworks
- MCP for the Model Context Protocol

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.
