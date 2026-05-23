# [ADR-005] Hybrid Hit Detection System
- **Status**: Accepted
- **Context**: The game features diverse weaponry and abilities. Standard firearms require immediate feedback, while throwable items (grenades) or special abilities require physical travel time and arcs.
- **Decision**: Implement a Hybrid Hit Detection architecture: *Hitscan* (instantaneous raycasting) for standard firearms, and *Server-Simulated Projectiles* (physics-based entities) for throwables and slow-moving abilities.
- **Considered Options**:
  - *Pure Projectile System*: Rejected because simulating physics for every single bullet fired by 20 players simultaneously would cause severe server CPU degradation.
  - *Pure Hitscan System*: Rejected as it limits game design; it cannot simulate arcing grenades or dodging mechanics for specific abilities.
- **Consequences**:
  - **Pros**: Balances server performance with rich gameplay variety. Optimizes processing power by only simulating physics where visually and mechanically necessary.
  - **Cons**: Requires maintaining two distinct hit validation, lag compensation, and rollback systems within the codebase.