```mermaid
flowchart LR
A[Výběr root dokumentu] --> B[Spuštění importu]
B --> C[Asynchronní import]
C --> D[Indexace]
D --> E[Dokument dostupný ve vyhledávání]
```
