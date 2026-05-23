# [ADR-002] Latency Mitigation via Client-Side Prediction and Server Reconciliation
- **Status**: Accepted
- **Context**: Network latency (ping) creates a delay between a player pressing a button and the server processing the action. If the client waits for the server's response to update the UI/camera, the game will feel sluggish and unplayable.
- **Decision**: Implement Client-Side Prediction for local movement and input, coupled with Server Reconciliation and Server-Side Lag Compensation (Rewind) for hit validation.
- **Considered Options**:
  - *Option 1: Pure Server-Authoritative execution.* Rejected because rendering actions only after server confirmation introduces noticeable input lag, ruining the competitive FPS experience.
  - *Option 2: Peer-to-Peer network topology.* Rejected due to inherent security flaws, high susceptibility to cheating, and unfair "host advantage."
- **Consequences**:
  - *Pros:* Players experience immediate visual feedback ("false input" validation), making the game feel highly responsive. The server remains the ultimate source of truth, maintaining security.
  - *Cons:* High codebase complexity. Requires the engine to maintain a historical buffer of game states to rewind and validate actions based on individual client latency.