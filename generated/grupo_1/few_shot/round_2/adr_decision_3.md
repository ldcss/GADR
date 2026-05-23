# [ADR-003] Hybrid Combat Resolution (Hitscan vs. Projectile)
- **Status**: Accepted
- **Context**: Processing complex physics trajectories for every fired bullet in a 10v10 match causes unnecessary CPU overhead on the server. However, certain tactical items (like grenades) absolutely require physics-based trajectories to function correctly within the game design.
- **Decision**: Adopt a hybrid combat calculation system utilizing Hitscan (instantaneous raycasting) for standard firearms and Projectile physics for arced or throwable items.
- **Considered Options**:
  - *Option 1: Pure Projectile System.* Rejected because calculating travel time, drop, and collision for every single machine-gun bullet across 20 players overloads server CPU and complicates lag compensation.
  - *Option 2: Pure Hitscan System.* Rejected because it removes the ability to have tactical throwable abilities that bounce off geometry or travel over time.
- **Consequences**:
  - *Pros:* Highly optimizes server performance for 90% of combat interactions (bullets) while preserving gameplay depth for specialized abilities.
  - *Cons:* The engine and netcode must maintain and synchronize two distinct hit-registration mechanisms simultaneously.