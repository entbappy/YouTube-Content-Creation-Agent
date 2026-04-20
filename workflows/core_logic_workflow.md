# Core Logic Workflow

```mermaid
flowchart TD
    A[Input Request] --> B[Validate Parameters]
    B -->|Valid| C[Extract Topic]
    B -->|Invalid| D[Return Error]

    C --> E[Information Retrieval]
    E --> F[Call Tavily API]
    F --> G[Process Search Results]
    G --> H[Filter Relevant Data]
    H --> I[Summarize Information]

    I --> J[Script Generation]
    J --> K[Prepare Prompt]
    K --> L[Call Gemini API]
    L --> M[Receive Generated Script]
    M --> N[Parse Script Structure]

    N --> O[Content Optimization]
    O --> P[Format for YouTube]
    P --> Q[Add Metadata]
    Q --> R[Generate Title]
    R --> S[Generate Description]
    S --> T[Generate Tags]

    T --> U[Package Results]
    U --> V[Return Response]

    D --> W[Error Handling]
    W --> X[Log Error]
    X --> Y[Format Error Response]
    Y --> V
```

## Core Processing Sequence

### Information Retrieval Process
```mermaid
sequenceDiagram
    participant Core as Core Logic
    participant Tavily as Tavily API
    participant Processor as Data Processor

    Core->>Tavily: Search request with topic
    Tavily-->>Core: Raw search results
    Core->>Processor: Filter and clean data
    Processor-->>Core: Processed information
    Core->>Processor: Summarize key points
    Processor-->>Core: Condensed information
```

### Script Generation Process
```mermaid
sequenceDiagram
    participant Core as Core Logic
    participant Gemini as Gemini API
    participant Formatter as Content Formatter

    Core->>Formatter: Create generation prompt
    Formatter-->>Core: Formatted prompt
    Core->>Gemini: Send prompt with context
    Gemini-->>Core: Generated script text
    Core->>Formatter: Parse script structure
    Formatter-->>Core: Structured script data
    Core->>Formatter: Add YouTube formatting
    Formatter-->>Core: Final script package
```

## Core Components

### Data Structures
```mermaid
classDiagram
    class ContentRequest {
        +topic: str
        +style: str
        +duration: int
        +audience: str
    }

    class SearchResults {
        +raw_data: list
        +sources: list
        +summary: str
    }

    class GeneratedContent {
        +script: str
        +title: str
        +description: str
        +tags: list
        +metadata: dict
    }

    ContentRequest --> CoreLogic
    CoreLogic --> SearchResults
    CoreLogic --> GeneratedContent
```

### Error Handling
```mermaid
flowchart TD
    A[Process Request] --> B{API Available?}
    B -->|No| C[Network Error]
    B -->|Yes| D{Check Quota}
    D -->|Exceeded| E[Quota Error]
    D -->|OK| F[Process Request]
    F --> G{Valid Response?}
    G -->|No| H[API Error]
    G -->|Yes| I[Success]

    C --> J[Log Error]
    E --> J
    H --> J
    J --> K[Return Error Response]
    I --> L[Return Success Response]
```

## Performance Considerations

### Caching Strategy
```mermaid
flowchart TD
    A[New Request] --> B{Cache Hit?}
    B -->|Yes| C[Return Cached Result]
    B -->|No| D[Process Request]
    D --> E[Store in Cache]
    E --> F[Return Result]
    C --> G[Update Cache Stats]
    F --> G
```

### Rate Limiting
```mermaid
stateDiagram-v2
    [*] --> Ready
    Ready --> Processing: Request Received
    Processing --> RateLimited: Rate Limit Exceeded
    Processing --> Completed: Request Processed
    Completed --> Ready: Reset Window
    RateLimited --> Waiting: Wait Period
    Waiting --> Ready: Period Expired
```