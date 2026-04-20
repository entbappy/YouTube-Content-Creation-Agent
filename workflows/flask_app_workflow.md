# Flask Web Application Workflow

```mermaid
sequenceDiagram
    participant User as User
    participant Browser as Web Browser
    participant Flask as Flask App
    participant Core as Core Logic
    participant Tavily as Tavily API
    participant Gemini as Gemini API

    User->>Browser: Open http://localhost:5000
    Browser->>Flask: GET /
    Flask-->>Browser: HTML Form Page

    User->>Browser: Fill form and submit
    Browser->>Flask: POST /generate
    Flask->>Core: Process request
    Core->>Tavily: Research topic
    Tavily-->>Core: Information data
    Core->>Gemini: Generate script
    Gemini-->>Core: Script content
    Core-->>Flask: Formatted results
    Flask-->>Browser: Results page with script

    Note over User,Browser: User can download or copy results
```

## Flask Application Flow

### Request Processing
```mermaid
flowchart TD
    A[HTTP Request] --> B{Route}
    B -->|/| C[Render Home Page]
    B -->|/generate| D[Process Generation Request]
    B -->|Other| E[404 Error]

    D --> F[Validate Input]
    F -->|Valid| G[Call Core Logic]
    F -->|Invalid| H[Return Error Page]

    G --> I[Generate Content]
    I --> J[Render Results Page]
    J --> K[Return HTML Response]
```

### Page Flow
```mermaid
stateDiagram-v2
    [*] --> HomePage
    HomePage --> Processing: Submit Form
    Processing --> ResultsPage: Generation Complete
    Processing --> ErrorPage: Generation Failed
    ResultsPage --> HomePage: Generate New
    ErrorPage --> HomePage: Try Again
    ResultsPage --> [*]: Close Browser
    ErrorPage --> [*]: Close Browser
```

## Flask Components

### Routes
- `GET /`: Home page with input form
- `POST /generate`: Process content generation
- `GET /health`: Health check endpoint

### Templates
- `index.html`: Main form page
- `results.html`: Results display page
- `error.html`: Error display page

### Static Files
- CSS for styling
- JavaScript for interactivity
- Images and assets