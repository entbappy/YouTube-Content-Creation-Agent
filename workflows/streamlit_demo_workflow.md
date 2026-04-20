# Streamlit Demo Workflow

```mermaid
sequenceDiagram
    participant User as User
    participant Streamlit as Streamlit App
    participant Core as Core Logic
    participant Tavily as Tavily API
    participant Gemini as Gemini API

    User->>Streamlit: Launch app
    Streamlit-->>User: Display interface

    User->>Streamlit: Enter topic
    User->>Streamlit: Select options
    User->>Streamlit: Click Generate

    Streamlit->>Core: Process request
    Core->>Tavily: Research topic
    Tavily-->>Core: Information data
    Core->>Gemini: Generate script
    Gemini-->>Core: Script content
    Core-->>Streamlit: Results

    Streamlit-->>User: Display script
    Streamlit-->>User: Show metadata

    Note over User,Streamlit: Interactive updates and feedback
```

## Streamlit Interface Flow

### App Structure
```mermaid
flowchart TD
    A[App Start] --> B[Set Page Config]
    B --> C[Load Environment]
    C --> D[Initialize APIs]
    D --> E[Render UI Components]
    E --> F[Handle User Interactions]
    F --> G{Generate Button Clicked?}
    G -->|Yes| H[Process Generation]
    G -->|No| F
    H --> I[Display Results]
    I --> F
```

### UI Components
```mermaid
flowchart LR
    A[Sidebar] --> B[Title Input]
    A --> C[Style Selector]
    A --> D[Duration Slider]
    A --> E[Generate Button]

    F[Main Area] --> G[Results Display]
    F --> H[Script Text Area]
    F --> I[Metadata Boxes]
    F --> J[Download Options]
```

## Streamlit Features

### Interactive Elements
- **Text Input**: Topic entry with validation
- **Radio Buttons**: Style selection
- **Slider**: Duration adjustment
- **Button**: Generation trigger
- **Text Area**: Script display (read-only)
- **Info Boxes**: Metadata display
- **Download Button**: Export functionality

### State Management
```mermaid
stateDiagram-v2
    [*] --> Initial
    Initial --> InputReady: Page Load
    InputReady --> Processing: Generate Click
    Processing --> ResultsReady: Generation Complete
    Processing --> ErrorState: Generation Failed
    ResultsReady --> InputReady: Reset/New Topic
    ErrorState --> InputReady: Try Again
    ResultsReady --> [*]: Close App
    ErrorState --> [*]: Close App
```

### Data Flow
```mermaid
flowchart TD
    A[User Input] --> B[Form Validation]
    B --> C[API Calls]
    C --> D[Result Processing]
    D --> E[UI Update]
    E --> F[Display Results]
    F --> G[User Interaction]
    G --> H{New Generation?}
    H -->|Yes| A
    H -->|No| I[End Session]
```