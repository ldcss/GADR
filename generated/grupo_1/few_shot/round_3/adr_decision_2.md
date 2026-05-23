# [ADR-002] Client-Side Prediction and Server Reconciliation for Game State
- **Status**: Accepted
- **Context**: Network latency (ping) between players and the game server introduces a delay. If a client waits for server validation before rendering an action (e.g., movement or shooting), the game will feel unresponsive. 
- **Decision**: Implement Client-Side Prediction coupled with Server Reconciliation, Entity Interpolation, and Server-Side Lag Compensation (rewind). The client will predict and render local movements instantly, while the authoritative server corrects the state asynchronously.
- **Considered Options**:
  - *Option 1: Pure authoritative server without client prediction.* Rejected because waiting for round-trip server confirmation before updating the UI creates an unplayable, laggy experience.
  - *Option 2: Peer-to-peer authoritative clients.* Rejected due to massive security risks (cheating) and the impossibility of resolving state conflicts reliably among 20 players.
- **Consequences**:
  - *Pros:* Masks network latency, providing players with immediate visual feedback and a smooth, highly responsive gameplay experience.
  - *Cons:* Introduces "rubber-banding" visual artifacts if the client prediction diverges significantly from the server's authoritative state. Greatly increases client-side codebase complexity due to the need for state history and rollback mechanisms.