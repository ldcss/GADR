# [ADR-001] Network Protocol Selection for Gameplay and Services
- **Status**: Accepted
- **Context**: The system is a competitive 10v10 online First-Person Shooter (FPS). Real-time state synchronization requires extremely low latency, whereas out-of-match services (like purchases or account management) require guaranteed data delivery.
- **Decision**: Utilize UDP for all real-time in-match gameplay data transmission, and restrict TCP exclusively to critical out-of-match transactions (e.g., payments, account authentication).
- **Considered Options**:
  - *Option 1: TCP for all communications.* Rejected because TCP's guaranteed delivery mechanics (packet acknowledgment and retransmission) cause head-of-line blocking, leading to unacceptable latency spikes during gameplay.
  - *Option 2: UDP for all communications.* Rejected because UDP does not guarantee delivery, which is unacceptable for sensitive operations like marketplace transactions or account state updates.
- **Consequences**:
  - *Pros:* Achieves the lowest possible latency for movement and combat events, maintaining a fluid competitive environment.
  - *Cons:* The client application must handle gameplay packet loss manually, requiring the implementation of UI indicators (e.g., packet loss icons) to inform the player of network instability.