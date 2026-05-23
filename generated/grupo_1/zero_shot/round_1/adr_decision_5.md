# [ADR-005] Network Traffic Optimization via Interest Management
- **Status**: Accepted
- **Context**: Broadcasting the real-time global state of the entire map and all 20 players to every single client consumes excessive bandwidth and client-side memory.
- **Decision**: We will implement Interest Management (Network/Occlusion Culling) on the server. The server will act as a spatial broker, only sending entity state and event updates to clients if they occur within a specific relevant radius of the player.
- **Considered Options**: 
  - **Global State Replication**: Rejected because sending updates about a firefight happening 2km away to a player who cannot see or interact with it wastes bandwidth and client processing power.
- **Consequences**: 
  - **Pros**: Greatly reduces network payload sizes; lowers client-side rendering and processing overhead; prevents "wallhack" cheats since the client never receives data for distant/hidden enemies.
  - **Cons**: Increases CPU load on the authoritative server, which must constantly calculate spatial hashing/distances to determine which data packets go to which clients.