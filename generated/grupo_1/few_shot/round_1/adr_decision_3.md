# [ADR-003] Hybrid Collision Detection System (Hitscan and Projectile)
- **Status**: Accepted
- **Context**: Calculating weapon ballistics is highly resource-intensive. Computing physics for every single bullet fired by 20 players simultaneously would overload the server. However, lacking physical arcs for throwables limits gameplay depth.
- **Decision**: Implement a hybrid combat calculation system: use Hitscan (instantaneous raycasting) for standard firearms, and simulated physics Projectiles for throwables (grenades) and special abilities.
- **Considered Options**:
  - *Option 1: 100% Projectile physics.* Rejected because calculating travel time, gravity, and collision for high-fire-rate automatic weapons causes unnecessary server strain.
  - *Option 2: 100% Hitscan.* Rejected because it prevents the implementation of arcing weapons, bouncy grenades, and specialized abilities, severely limiting game design.
- **Consequences**:
  - *Pros:* Optimizes server performance by offloading the majority of combat processing to cheap raycasts, while preserving tactical gameplay depth for specific items.
  - *Cons:* Requires maintaining and synchronizing two distinct hit-registration and replication pipelines within the netcode.