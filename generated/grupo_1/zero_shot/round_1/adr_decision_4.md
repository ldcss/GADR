# [ADR-004] Hybrid Weapon Mechanics (Hitscan vs. Projectile)
- **Status**: Accepted
- **Context**: The game features different types of attacks. Simulating physics for every single bullet fired by 20 players is highly resource-intensive for the server. However, certain weapons (like grenades) require physical arcs.
- **Decision**: We will use a hybrid hit registration system: standard firearms will use Hitscan (instantaneous raycast validation), while throwables and special abilities will use Projectile physics (simulated object velocity and gravity over time).
- **Considered Options**: 
  - **Pure Projectile System**: Rejected due to the massive CPU overhead required on the server to track hundreds of bullet instances simultaneously.
  - **Pure Hitscan System**: Rejected because it cannot accurately simulate arcing weapons like grenades or rockets.
- **Consequences**: 
  - **Pros**: Drastically reduces server load by optimizing standard gunfire, while maintaining gameplay depth for tactical utility items.
  - **Cons**: Requires the engineering team to build, maintain, and test two separate hit registration and collision systems.