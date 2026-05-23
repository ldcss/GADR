# [ADR-002] Hybrid Weapon Hit Registration System
- **Status**: Accepted
- **Context**: The game features various weapon types, including standard firearms and throwable abilities (e.g., grenades, axes). Tracking every single bullet as a physical object in the game world consumes excessive server resources and adds unnecessary latency.
- **Decision**: Implement a hybrid hit registration system utilizing both Hitscan and Projectile physics.
- **Considered Options**:
  - *Pure Projectile System*: Rejected. Simulating physics for every single bullet fired in a 20-player match would overload the server's CPU and increase bandwidth consumption.
  - *Pure Hitscan System*: Rejected. Prevents the implementation of arced/throwable utility items (like grenades), limiting gameplay depth.
- **Consequences**:
  - **Pros**: Optimizes server performance by using instantaneous raycasting (Hitscan) for standard firearms, while reserving CPU-intensive physics calculations (Projectile) strictly for slow-moving or arcing abilities.
  - **Cons**: Requires maintaining two separate collision and validation pipelines within the game engine and server logic.