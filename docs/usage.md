# Usage Guide

This guide explains how to use the YouTube Content Creation Agent in different modes.

## Overview

The YouTube Content Creation Agent provides three main interfaces:

1. **MCP Server**: For integration with AI assistants
2. **Flask Web Application**: User-friendly web interface
3. **Streamlit Demo**: Quick demonstration interface

## MCP Server Mode

The MCP (Model Context Protocol) server allows AI assistants to interact with the content creation tools.

### Starting the MCP Server

```bash
# Using UV
uv run mcp dev mcp_server.py

# Using standard Python
python mcp_server.py
```

### Available Tools

The MCP server provides the following tools:

- **get_real_time_info**: Retrieves current information about a topic using web search
- **generate_video_script**: Creates a complete video script based on research and topic

### Integration with AI Assistants

Once the MCP server is running, AI assistants can connect to it and use the tools for content creation workflows.

## Flask Web Application

The Flask web app provides a user-friendly interface for content creation.

### Starting the Web App

```bash
# Using UV
uv run python flask_app.py

# Using standard Python
python flask_app.py
```

### Accessing the Web Interface

1. Open your browser
2. Navigate to `http://localhost:5000` (or the port shown in the console)
3. Enter your topic or content requirements
4. Click "Generate" to create content

### Features

- **Topic Input**: Enter any topic you want to create content about
- **Real-time Research**: Automatically gathers current information
- **Script Generation**: Creates engaging video scripts
- **Download Options**: Export generated content

## Streamlit Demo

The Streamlit demo provides an interactive interface for testing and demonstration.

### Starting the Demo

```bash
# Using UV
uv run streamlit run demo.py

# Using standard Python
streamlit run demo.py
```

### Using the Demo Interface

1. The app will open in your default browser automatically
2. Enter a topic in the text input field
3. Adjust any parameters if available
4. Click the generate button
5. View the results and generated script

## Core Functionality

### Information Retrieval

The agent uses the Tavily API to gather real-time information about topics:

- Searches multiple sources for current data
- Filters and summarizes relevant information
- Provides context for script generation

### Script Generation

Using Google's Gemini 2.0 Flash model:

- Analyzes gathered information
- Creates engaging video scripts
- Structures content for YouTube format
- Optimizes for viewer engagement

## Advanced Usage

### Customizing Scripts

You can modify the script generation by:

- Providing specific guidelines in your topic description
- Adjusting the tone and style requirements
- Specifying target audience
- Including specific elements to cover

### Batch Processing

For processing multiple topics:

1. Use the MCP server mode for programmatic access
2. Create scripts for multiple topics in sequence
3. Store results for later use

## Examples

### Example 1: Technology Topic

**Input Topic**: "Latest developments in quantum computing"

**Process**:
1. Agent searches for recent quantum computing news
2. Gathers information from reliable sources
3. Generates a script explaining key developments
4. Structures the script with introduction, main content, and conclusion

### Example 2: Educational Content

**Input Topic**: "How photosynthesis works for kids"

**Process**:
1. Researches simplified explanations of photosynthesis
2. Creates age-appropriate content
3. Generates engaging script with visuals suggestions
4. Includes interactive elements for educational value

## Performance Tips

- **API Rate Limits**: Be aware of API rate limits for both Gemini and Tavily
- **Content Length**: Longer topics may take more time to process
- **Network Connection**: Ensure stable internet for real-time research
- **System Resources**: The agent requires sufficient RAM for processing

## Troubleshooting

### Common Issues

1. **Server not starting**
   - Check that all dependencies are installed
   - Verify API keys are correctly set
   - Ensure ports are not in use

2. **Generation errors**
   - Check API key validity
   - Verify internet connection
   - Review error messages in console

3. **Slow performance**
   - Use UV for faster dependency management
   - Ensure sufficient system resources
   - Consider using lighter models if available

### Logs and Debugging

- Check console output for error messages
- Review API usage in your dashboard
- Enable debug mode if available in future versions