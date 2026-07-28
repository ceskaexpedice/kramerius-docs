```mermaid
sequenceDiagram
    participant Uživatel
    participant Search Endpoint
    participant Solr Engine
    
    Uživatel->>Search Endpoint: 1. Poslání požadavku
    Search Endpoint->>Search Endpoint: 2. Validace parametrů
    Search Endpoint->>Solr Engine: 3. Poslání požadavku
    Solr Engine-->>Search Endpoint: 4. Odpověď
    Search Endpoint->>Search Endpoint: 5. Ořezání chráněných dat
    Search Endpoint-->>Uživatel: 6. Odeslání odpovědi
```

