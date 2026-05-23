# [ADR-004] UDP Transport Protocol for Real-Time Gameplay Data
- **Status**: Accepted
- **Context**: Real-time FPS games require constant, high-speed transmission of positional and event data. Waiting for packet delivery confirmation causes latency spikes, which is detrimental to fast-paced competitive gameplay. 
- **Decision**: Use UDP (User Datagram Protocol) as the primary transport protocol for real-time game state updates and player inputs. (Note: Critical asynchronous transactions, such as marketplace purchases, will utilize a reliable protocol like TCP, but core gameplay defaults to UDP).
- **Considered Options**:
  - *Option 1: TCP (Transmission Control Protocol) for all communications.* Rejected for core gameplay data because its built-in error checking, packet ordering, and retransmission mechanisms introduce unacceptable latency overhead.
- **Consequences**:
  - *Pros:* Provides the lowest possible network latency, ensuring fast state updates suitable for a competitive FPS environment.
  - *Cons:* UDP does not guarantee packet delivery or order. The application layer must be built to handle packet loss gracefully via state snapshots, extrapolation, and interpolation.