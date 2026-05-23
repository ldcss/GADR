# [ADR-004] Bandwidth Optimization via Interest Management
- **Status**: Accepted
- **Context**: Broadcasting the state of all 20 players, projectiles, and dynamic entities across a large map to every single client consumes excessive server CPU and outbound bandwidth.
- **Decision**: Implement Interest Management (Distance/Occlusion Culling) via an event observer/broker pattern on the game server. Clients will only receive state updates for entities within their relevant interaction radius (e.g., line of sight or auditory range).
- **Considered Options**:
  - *Global State Broadcast*: Rejected because it wastes bandwidth on irrelevant data (e.g., a fight happening 2km away) and exposes the system to "Wallhack" / ESP cheats, as clients hold data for unseen enemies.
- **Consequences**:
  - **Pros**: Drastically reduces network bandwidth consumption and client-side processing load. Significantly improves security by starving cheaters of global map data.
  - **Cons**: Increases server CPU load, as the server must continuously calculate spatial relevance for all 20 players every tick.