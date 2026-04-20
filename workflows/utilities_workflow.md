# Utilities Workflow

```mermaid
graph TB
    A[Main Application] --> B[Pydantic Models]
    A --> C[Query Validation]
    A --> D[Logging System]
    A --> E[Memory Management]

    B --> F[Request Models]
    B --> G[Response Models]
    F --> H[Input Validation]
    G --> I[Output Formatting]

    C --> J[Query Processing]
    C --> K[Query Transformation]
    J --> L[Sanitization]
    K --> M[Optimization]

    D --> N[Log Configuration]
    D --> O[Log Handlers]
    N --> P[File Logging]
    N --> Q[Console Logging]
    O --> R[Structured Logging]

    E --> S[Mem0 Integration]
    E --> T[Memory Storage]
    S --> U[Context Retrieval]
    T --> V[Persistent Storage]
```

## Utility Modules Overview

### Pydantic Models
```mermaid
classDiagram
    class BaseRequest {
        +topic: str
        +validate_topic()
    }

    class ContentRequest {
        +style: str
        +duration: int
        +audience: str
    }

    class APIResponse {
        +success: bool
        +data: dict
        +error: str
    }

    class ScriptResponse {
        +script: str
        +title: str
        +description: str
        +tags: list
    }

    BaseRequest <|-- ContentRequest
    APIResponse <|-- ScriptResponse
```

### Query Validation & Transformation
```mermaid
flowchart TD
    A[Raw Query] --> B[Input Sanitization]
    B --> C[Length Validation]
    C --> D[Content Filtering]
    D --> E[Query Optimization]
    E --> F[Context Enhancement]
    F --> G[Validated Query]

    G --> H{Valid?}
    H -->|Yes| I[Process Query]
    H -->|No| J[Return Error]
```

### Logging System
```mermaid
flowchart TD
    A[Application Event] --> B[Log Level Check]
    B --> C{Level >= Threshold?}
    C -->|Yes| D[Format Message]
    C -->|No| E[Discard]

    D --> F[Add Context]
    F --> G[Write to Handlers]
    G --> H[File Handler]
    G --> I[Console Handler]
    G --> J[External Handler]

    H --> K[Rotate Files]
    I --> L[Color Coding]
    J --> M[Send to Service]
```

### Memory Management (Mem0)
```mermaid
sequenceDiagram
    participant App as Application
    participant Mem0 as Mem0 Service
    participant Store as Memory Store

    App->>Mem0: Store context
    Mem0->>Store: Save data
    Store-->>Mem0: Confirmation

    App->>Mem0: Retrieve context
    Mem0->>Store: Query data
    Store-->>Mem0: Retrieved data
    Mem0-->>App: Context results

    App->>Mem0: Update memory
    Mem0->>Store: Update data
    Store-->>Mem0: Update confirmation
```

## Utility Integration Flow

### Application Startup
```mermaid
flowchart TD
    A[App Start] --> B[Load Config]
    B --> C[Initialize Logging]
    C --> D[Setup Pydantic Models]
    D --> E[Configure Mem0]
    E --> F[Validate Environment]
    F --> G[Ready for Requests]
```

### Request Processing with Utilities
```mermaid
flowchart TD
    A[Incoming Request] --> B[Validate with Pydantic]
    B --> C[Log Request Details]
    C --> D[Transform Query]
    D --> E[Check Memory Context]
    E --> F[Process with Context]
    F --> G[Store New Context]
    G --> H[Log Processing Results]
    H --> I[Format Response]
    I --> J[Return Response]
```

## Configuration and Setup

### Logging Configuration
```yaml
logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  handlers:
    - file:
        filename: app.log
        maxBytes: 10485760
        backupCount: 5
    - console:
        level: DEBUG
```

### Mem0 Configuration
```python
mem0_config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "youtube_agent_memory",
            "path": "./db"
        }
    },
    "llm": {
        "provider": "openai",  # or other providers
        "config": {
            "model": "gpt-4",
            "temperature": 0.1
        }
    }
}
```

## Testing Utilities

### Unit Test Coverage
```mermaid
graph LR
    A[Utility Tests] --> B[Pydantic Tests]
    A --> C[Validation Tests]
    A --> D[Logging Tests]
    A --> E[Memory Tests]

    B --> F[Model Validation]
    B --> G[Serialization]
    C --> H[Query Sanitization]
    C --> I[Transformation Logic]
    D --> J[Log Formatting]
    D --> K[Handler Testing]
    E --> L[Memory Storage]
    E --> M[Context Retrieval]
```

## Performance Monitoring

### Metrics Collection
- Request validation time
- Query transformation duration
- Memory retrieval latency
- Log processing overhead
- Error rates by utility

### Health Checks
- Pydantic model loading
- Logging system availability
- Memory store connectivity
- Configuration validation