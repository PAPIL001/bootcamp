# Login Flow Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database

    User->>Frontend: Enters username and password
    Frontend->>Backend: Sends login request (username, password)
    Backend->>Database: Authenticates user (checks username and password)
    Database-->>Backend: Authentication result (success/failure)
    alt Authentication successful
        Backend->>Frontend: Login success
        Frontend->>User: User logged in
    else Authentication failed
        Backend->>Frontend: Login failure
        Frontend->>User: Authentication failed message
    end
