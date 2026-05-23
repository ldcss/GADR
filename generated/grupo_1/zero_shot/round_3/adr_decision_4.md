# [ADR-004] Network Bandwidth Optimization via Interest Management
- **Status**: Accepted
- **Context**: Broadcasting the precise state, movement, and actions of all 20 players to every client simultaneously wastes bandwidth. Clients do not need high-frequency updates for events occurring on the opposite side of the map.
- **Decision**: Implement Spatial Partitioning/Interest Management (network-level occlusion culling). A message broker pattern will be used on the server to distribute positional data only to clients within a relevant physical radius.
- **Considered Options**:
  - *Global State Replication*: Rejected. Sending complete world states to all clients scales poorly, increases server bandwidth costs, and exposes hidden enemy positions to client memory (enabling "wallhack" cheats).
- **Consequences**:
  - **Pros**: Significantly reduces data payloads per client tick. Enhances security by withholding irrelevant enemy data from potential cheaters.
  - **Cons**: Increases server-side CPU load, as the server must continuously calculate the distance, line-of-sight, and relevance of events for each individual client before dispatching the state snapshot.