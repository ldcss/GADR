# [ADR-001] Client-Server Architecture over UDP with Asynchronous State Streaming
- **Status**: Accepted
- **Context**: The system is a competitive 10v10 online First-Person Shooter (FPS). Real-time communication is critical. Traditional synchronous requests block execution, and guaranteed packet delivery protocols introduce latency that degrades player experience during fast-paced combat. 
- **Decision**: Adopt a strict Client-Server architecture utilizing UDP for asynchronous, continuous data streaming (event state updates) between clients and the server.
- **Considered Options**:
  - *Option 1: TCP.* Rejected because packet confirmation and retransmission mechanisms cause head-of-line blocking, leading to unacceptable latency spikes and stuttering.
  - *Option 2: Synchronous HTTP polling.* Rejected because the overhead of establishing connections and waiting for responses is incompatible with real-time frame rates.
- **Consequences**:
  - *Pros:* Achieves the lowest possible latency for game state delivery. Outdated packets can be safely ignored without network clogging.
  - *Cons:* Requires custom application-layer implementation to ensure reliability for critical, non-reoccurring events (e.g., match connection, final kill confirmation).