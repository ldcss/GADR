# [ADR-002] Real-Time Gameplay Network Protocol
- **Status**: Accepted
- **Context**: The game client and server must exchange continuous streams of positional, rotational, and action data at high tick rates. Guaranteed delivery of every single packet is less important than receiving the most up-to-date state as fast as possible.
- **Decision**: Use UDP (User Datagram Protocol) for all real-time in-game communication (movement, shooting, state snapshots).
- **Considered Options**:
  - *TCP (Transmission Control Protocol)*: Rejected because its guaranteed delivery mechanism causes head-of-line blocking. A single dropped packet halts the entire stream, resulting in severe gameplay stuttering.
  - *WebSockets*: Rejected for gameplay loops due to TCP-underpinnings, though it may be used for out-of-game chat or matchmaking.
- **Consequences**:
  - **Pros**: Lowest possible latency; removes overhead from connection handshakes and packet acknowledgement.
  - **Cons**: The application layer must handle packet loss. Critical events (like match start/end) will require custom acknowledgment logic implemented over UDP.