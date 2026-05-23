# [ADR-001] Client-Server State Synchronization Strategy
- **Status**: Accepted
- **Context**: The system is a competitive 10v10 online FPS. Network latency can severely degrade the player experience. Waiting for server confirmation for every action (strict synchronous architecture) introduces noticeable input delay, making the game unplayable. 
- **Decision**: Implement an authoritative client-server architecture utilizing an asynchronous data stream with Client-Side Prediction, Server Reconciliation, and Lag Compensation (Rewind).
- **Considered Options**:
  - *Strict Synchronous Server Authority*: Rejected. Causes severe input lag; players would feel delays between button presses and on-screen actions.
  - *Peer-to-Peer (P2P)*: Rejected. Unsuitable for competitive FPS games due to high vulnerability to cheating and host-migration issues.
- **Consequences**:
  - **Pros**: Masks network latency effectively; provides immediate visual feedback ("false input") to the user, creating a smooth gameplay experience.
  - **Cons**: High implementation complexity. Will result in occasional visual anomalies (e.g., rubber-banding or "character freezing") when the client's predicted state diverges significantly from the authoritative server state.