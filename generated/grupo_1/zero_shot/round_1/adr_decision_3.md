# [ADR-003] Game State Synchronization and Latency Compensation
- **Status**: Accepted
- **Context**: Players will have varying pings based on their geographic location. Relying strictly on round-trip server communication for movement and actions results in noticeable input lag and "freezing" characters.
- **Decision**: We will implement Client-Side Prediction with Server Reconciliation, combined with Server Lag Compensation (rewind) and Entity Interpolation.
- **Considered Options**: 
  - **Strict Server Authority (No Prediction)**: Rejected because the game would feel unresponsive to the player due to network latency.
  - **Peer-to-Peer (Client Authority)**: Rejected due to the extreme risk of cheating and manipulation in a competitive environment.
- **Consequences**: 
  - **Pros**: Provides a smooth, responsive experience for the player; masks network latency effectively.
  - **Cons**: High implementation complexity. Will occasionally result in visual artifacts like "rubber-banding" when the server overrides a client's invalid predicted state.