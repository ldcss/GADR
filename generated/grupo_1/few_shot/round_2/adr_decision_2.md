# [ADR-002] Client-Server State Synchronization and Latency Mitigation
- **Status**: Accepted
- **Context**: In a distributed asynchronous environment, waiting for server validation before updating the client's screen results in perceived input lag, making an FPS unplayable. Furthermore, differing latencies among 20 players lead to inconsistent hit registration.
- **Decision**: Implement a combination of Client-Side Prediction, Server Reconciliation, and Lag Compensation (Server Rewind).
- **Considered Options**:
  - *Option 1: Strict Server Authority (No Prediction).* Rejected because players would experience a noticeable delay between pressing a button and their character moving, ruining the game feel.
  - *Option 2: Peer-to-Peer or Client Authority.* Rejected because trusting the client with hit registration and movement opens the system to trivial cheating and manipulation.
- **Consequences**:
  - *Pros:* Provides a seamless, immediate response to player inputs (false input buffer hides network delay) while maintaining a secure, authoritative server state. 
  - *Cons:* High implementation complexity. The server must retain a buffer of past game states to perform time-rewind calculations for hit validation, increasing memory consumption.