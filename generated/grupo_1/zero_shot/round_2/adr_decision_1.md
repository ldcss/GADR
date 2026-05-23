# [ADR-001] Network Gameplay Architecture and State Synchronization
- **Status**: Accepted
- **Context**: The system is a competitive 10v10 online FPS game. It requires highly responsive gameplay, minimal perceived latency, and strict prevention of cheating. Network fluctuations (lag, packet loss) must not disrupt the core player experience.
- **Decision**: Implement an Authoritative Client-Server architecture utilizing Client-Side Prediction, Server Reconciliation, Entity Interpolation/Extrapolation, and Lag Compensation (Rewind).
- **Considered Options**:
  - *Peer-to-Peer (P2P) Lockstep*: Rejected due to high vulnerability to cheating, host advantage, and poor handling of variable network latency among 20 players.
  - *Strict Synchronous Server Authority (No Client Prediction)*: Rejected because the input delay (waiting for server round-trip) makes FPS gameplay feel sluggish and unplayable.
- **Consequences**:
  - **Pros**: Ensures a smooth, responsive experience for players even under moderate lag. The server remains the ultimate source of truth, heavily mitigating cheating (e.g., speed hacks).
  - **Cons**: High implementation complexity. Requires maintaining historical buffers of game states and complex reconciliation logic to correct client states without visual snapping.