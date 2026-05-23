# [ADR-004] Network Traffic Optimization via Interest Management
- **Status**: Accepted
- **Context**: Broadcasting the entire world state to all 20 players simultaneously consumes excessive bandwidth. If two players are engaging in combat on one side of a large map, players 2 kilometers away do not need real-time micro-updates of that specific engagement.
- **Decision**: Implement spatial Interest Management (Occlusion/Distance Culling) using an in-match event broker to route state updates strictly to clients within a relevant proximity or line-of-sight.
- **Considered Options**:
  - *Option 1: Global State Broadcast.* Rejected because it wastes bandwidth, overloads client rendering, and makes wall-hack cheats much easier to create since clients possess all enemy coordinates at all times.
  - *Option 2: Strict Client-Side Culling.* Rejected because the server still sends the data, meaning network bandwidth is still wasted before the client discards the rendering task.
- **Consequences**:
  - *Pros:* Drastically reduces network payload sizes and client processing requirements, ensuring scalable performance even with detailed environments.
  - *Cons:* Adds computational overhead to the game server, which must continuously calculate spatial relevance (distance/zones) for all entities before dispatching network packets.