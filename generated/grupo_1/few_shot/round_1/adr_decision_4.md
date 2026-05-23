# [ADR-004] Spatial Interest Management (Network Culling)
- **Status**: Accepted
- **Context**: Broadcasting the exact position and state of all 20 players, plus world entities, to every client at all times consumes excessive bandwidth and client CPU resources. A player does not need granular data on a firefight happening 2km away on the map.
- **Decision**: Implement a Spatial Interest Management system (Occlusion/Distance Network Culling) acting as a broker to filter and route state updates based on client proximity and line-of-sight relevance.
- **Considered Options**:
  - *Option 1: Global state broadcasting.* Rejected because the exponential increase in bandwidth usage scales poorly and impacts performance on lower-end client machines.
- **Consequences**:
  - *Pros:* Drastic reduction in server bandwidth usage and client-side processing load. Prevents clients from extracting data to power "wall-hack" cheats for distant players.
  - *Cons:* Edge-case desyncs can occur if a fast-moving entity suddenly enters a player's area of interest, requiring careful tuning of the culling radius.