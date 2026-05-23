# [ADR-003] Interest Management and Spatial Filtering for State Updates
- **Status**: Accepted
- **Context**: Transmitting every single game event (e.g., footsteps, gunfire, state changes) to all 20 players simultaneously consumes massive bandwidth and client CPU, especially for events occurring far outside a player's field of view or interaction range.
- **Decision**: Implement server-side Interest Management (Spatial Partitioning / Data Culling) to filter and route game state updates only to players within a relevant geographical radius (e.g., a 1km in-game radius).
- **Considered Options**:
  - *Option 1: Broadcast all events to all clients continuously.* Rejected because it wastes bandwidth and drastically degrades client performance by forcing local machines to process irrelevant data.
- **Consequences**:
  - *Pros:* Drastically reduces network traffic and client-side processing load, enabling smoother performance and lower memory usage.
  - *Cons:* Adds continuous computational overhead to the server, which must constantly calculate distances and determine relevance for every entity relative to every player.