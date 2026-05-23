# [ADR-003] Network Protocol Selection
- **Status**: Accepted
- **Context**: Real-time multiplayer games require rapid, continuous updates of positional and state data. A dropped packet regarding a player's position a fraction of a second ago is immediately outdated by the next packet. However, out-of-match actions (payments, account data) require guaranteed delivery.
- **Decision**: Utilize UDP for in-game state streaming and positional updates, and TCP for critical out-of-match transactions (e.g., marketplace purchases, cross-region account synchronization).
- **Considered Options**:
  - *Pure TCP*: Rejected. The overhead of connection handshakes and guaranteed packet delivery (head-of-line blocking) introduces unacceptable latency for real-time FPS movement.
  - *Pure UDP*: Rejected. While optimal for game state, it is inherently unreliable and unacceptable for sensitive data like financial transactions or permanent account state changes.
- **Consequences**:
  - **Pros**: Maximizes gameplay responsiveness by firing-and-forgetting state packets. Secures critical player data via TCP reliability.
  - **Cons**: Requires the implementation of application-level packet loss handling (e.g., entity interpolation, extrapolation, and packet sequence identifiers) to smooth out lost UDP packets.