# API Reference

This document provides technical details about the YouTube Content Creation Agent's APIs and interfaces.

## MCP Server API

The MCP (Model Context Protocol) server exposes tools that can be used by AI assistants and other MCP-compatible clients.

### Server Configuration

- **Protocol Version**: MCP 1.0
- **Transport**: Stdio (for development), HTTP (for production)
- **Tools**: 2 available tools

### Available Tools

#### 1. get_real_time_info

Retrieves current information about a specified topic using web search.

**Parameters:**
- `topic` (string, required): The topic to research
- `max_results` (integer, optional): Maximum number of search results (default: 5)

**Returns:**
- `information` (string): Compiled information from web sources
- `sources` (array): List of source URLs used

**Example Usage:**
```json
{
  "tool": "get_real_time_info",
  "parameters": {
    "topic": "artificial intelligence trends 2024",
    "max_results": 10
  }
}
```

#### 2. generate_video_script

Creates a complete YouTube video script based on research and topic analysis.

**Parameters:**
- `topic` (string, required): The main topic for the video
- `style` (string, optional): Script style ("educational", "entertainment", "news")
- `duration` (integer, optional): Target video duration in minutes
- `audience` (string, optional): Target audience ("general", "experts", "beginners")

**Returns:**
- `script` (string): Complete video script with timestamps
- `title` (string): Suggested video title
- `description` (string): YouTube description
- `tags` (array): Suggested tags

**Example Usage:**
```json
{
  "tool": "generate_video_script",
  "parameters": {
    "topic": "How quantum computers work",
    "style": "educational",
    "duration": 10,
    "audience": "beginners"
  }
}
```

## Flask Web API

The Flask application provides a REST API for programmatic access.

### Endpoints

#### POST /generate

Generates content based on the provided parameters.

**Request Body:**
```json
{
  "topic": "string",
  "style": "educational|entertainment|news",
  "duration": 10,
  "audience": "general|experts|beginners"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "script": "Complete script text...",
    "title": "Video title",
    "description": "YouTube description",
    "tags": ["tag1", "tag2"]
  }
}
```

**Status Codes:**
- 200: Success
- 400: Bad Request (invalid parameters)
- 500: Internal Server Error

#### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

## Streamlit Interface

The Streamlit demo provides an interactive web interface.

### Components

#### Topic Input
- **Type**: Text input
- **Validation**: Required, minimum 3 characters
- **Placeholder**: "Enter your video topic here..."

#### Style Selection
- **Type**: Radio buttons
- **Options**: Educational, Entertainment, News
- **Default**: Educational

#### Duration Slider
- **Type**: Slider
- **Range**: 5-30 minutes
- **Default**: 10 minutes

#### Generate Button
- **Type**: Primary button
- **Action**: Triggers content generation
- **State**: Disabled during processing

### Output Components

#### Script Display
- **Type**: Text area (read-only)
- **Features**: Copy to clipboard, download as text

#### Metadata Display
- **Type**: Info boxes
- **Content**: Title, description, tags

## Core Module API

### Information Retrieval Module

#### Class: InfoRetriever

```python
from app import InfoRetriever

retriever = InfoRetriever(api_key="your_tavily_key")
results = retriever.search(topic="AI trends", max_results=5)
```

**Methods:**
- `search(topic, max_results=5)`: Performs web search
- `summarize(results)`: Summarizes search results

### Script Generation Module

#### Class: ScriptGenerator

```python
from app import ScriptGenerator

generator = ScriptGenerator(api_key="your_gemini_key")
script = generator.generate(topic="Quantum computing", style="educational")
```

**Methods:**
- `generate(topic, style="educational", duration=10)`: Generates video script
- `optimize_for_youtube(script)`: Optimizes script for YouTube format

## Configuration

### Environment Variables

- `GEMINI_API_KEY`: Google Generative AI API key
- `TAVILY_API_KEY`: Tavily API key
- `FLASK_PORT`: Port for Flask app (default: 5000)
- `STREAMLIT_PORT`: Port for Streamlit app (default: 8501)

### Model Configuration

- **Primary Model**: gemini-2.0-flash
- **Temperature**: 0.7 (for creativity)
- **Max Tokens**: 4096
- **Safety Settings**: Configured for content generation

## Error Handling

### Common Error Codes

- `API_KEY_MISSING`: Required API key not provided
- `API_QUOTA_EXCEEDED`: API usage limit reached
- `INVALID_TOPIC`: Topic validation failed
- `GENERATION_FAILED`: Content generation error
- `NETWORK_ERROR`: Connection issues

### Error Response Format

```json
{
  "success": false,
  "error": {
    "code": "API_KEY_MISSING",
    "message": "Gemini API key is required",
    "details": "Please set GEMINI_API_KEY in your .env file"
  }
}
```

## Rate Limits

- **Tavily API**: 1000 requests/day (free tier)
- **Gemini API**: Varies by model and billing
- **MCP Server**: No internal rate limits
- **Flask API**: 100 requests/minute per IP

## Data Flow

1. **Input Validation**: Topic and parameters validated
2. **Information Retrieval**: Web search using Tavily
3. **Data Processing**: Results filtered and summarized
4. **Script Generation**: Gemini model creates script
5. **Output Formatting**: Script formatted for YouTube
6. **Response**: Formatted data returned to client

## Security Considerations

- API keys stored securely in environment variables
- Input validation to prevent injection attacks
- Rate limiting to prevent abuse
- HTTPS recommended for production deployment