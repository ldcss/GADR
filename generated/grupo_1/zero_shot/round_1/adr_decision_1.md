# [ADR-001] Network Transport Protocol (UDP)
- **Status**: Accepted
- **Context**: The system is a real-time, 10v10 online competitive First-Person Shooter (FPS). In this environment, ultra-low latency is critical, and waiting for dropped packets to be retransmitted creates unacceptable gameplay lag.
- **Decision**: We will use UDP (User Datagram Protocol) for continuous, real-time game state transmission between the client and the server.
- **Considered Options**: 
  - **TCP (Transmission Control Protocol)**: Rejected because its guaranteed delivery mechanism causes head-of-line blocking. Retransmitting dropped packets introduces latency spikes that ruin the real-time FPS experience.
- **Consequences**: 
  - **Pros**: Minimal latency; avoids blocking the data stream when packets are lost.
  - **Cons**: Packet loss is expected. The application layer must handle missing data via interpolation, and critical events (like match ends or payments) will require a separate, reliable transmission layer.