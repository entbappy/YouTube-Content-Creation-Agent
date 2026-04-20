# System Architecture Workflow

```mermaid
graph TB
    A[User Input] --> B{Interface Choice}
    B -->|MCP Server| C[MCP Server]
    B -->|Flask Web| D[Flask App]
    B -->|Streamlit Demo| E[Streamlit App]

    C --> F[Core Logic]
    D --> F
    E --> F

    F --> G[Information Retrieval]
    F --> H[Script Generation]

    G --> I[Tavily API]
    H --> J[Gemini API]

    I --> K[Web Search Results]
    J --> L[Generated Script]

    K --> M[Data Processing]
    L --> M

    M --> N[Output Formatting]
    N --> O[Final Content]

    O --> P{Output Destination}
    P -->|MCP Response| Q[MCP Client]
    P -->|Web Display| R[Browser]
    P -->|Streamlit UI| S[Streamlit Interface]
```

## Workflow Description

1. **User Input**: User provides topic and parameters through chosen interface
2. **Interface Selection**: Choose between MCP server, Flask web app, or Streamlit demo
3. **Core Processing**: All interfaces route to the core application logic
4. **Information Retrieval**: Use Tavily API to gather real-time web data
5. **Script Generation**: Use Gemini API to create video scripts
6. **Data Processing**: Combine and process retrieved information and generated content
7. **Output Formatting**: Format final content for the target platform
8. **Delivery**: Return results through the appropriate interface