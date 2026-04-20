# Installation Guide

This guide provides detailed instructions for installing the YouTube Content Creation Agent.

## Prerequisites

- Python 3.13 or higher
- Git (for cloning the repository)

## API Keys Required

Before running the application, you'll need to obtain API keys for the following services:

### Google Generative AI (Gemini)
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new project or select an existing one
3. Generate an API key from the API keys section
4. Copy the API key for use in the `.env` file

### Tavily API
1. Visit [Tavily](https://tavily.com/)
2. Sign up for an account
3. Generate an API key from your dashboard
4. Copy the API key for use in the `.env` file

## Installation Methods

### Method 1: Standard Python Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd youtube-content-creation-agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Method 2: UV Package Manager (Recommended)

UV is a fast Python package manager that can significantly speed up installation.

1. **Install UV**
   ```bash
   # Using pip
   pip install uv

   # Or on Windows using winget
   winget install astral-sh.uv

   # Or using other methods from https://github.com/astral-sh/uv
   ```

2. **Clone and setup with UV**
   ```bash
   git clone <repository-url>
   cd youtube-content-creation-agent
   uv sync
   ```

## Configuration

1. **Create environment file**
   ```bash
   # Create .env file in the root directory
   touch .env
   ```

2. **Add your API keys to .env**
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   TAVILY_API_KEY=your_actual_tavily_api_key_here
   ```

## Verification

After installation, verify everything is working:

```bash
# Test Python version
python --version

# Test imports
python -c "import google.generativeai; import tavily; print('All imports successful')"
```

## Troubleshooting

### Common Issues

1. **Python version too old**
   - Ensure you're using Python 3.13 or higher
   - Check with `python --version`

2. **Virtual environment not activated**
   - Make sure to activate the virtual environment before running commands
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

3. **API key issues**
   - Verify API keys are correctly added to `.env` file
   - Ensure no extra spaces or characters in the `.env` file

4. **Permission errors**
   - On Windows, run terminal as administrator if needed
   - On Linux/macOS, check file permissions

### Getting Help

If you encounter issues not covered here, please:
1. Check the [GitHub Issues](https://github.com/your-repo/issues) page
2. Open a new issue with detailed error messages and your system information