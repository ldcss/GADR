# [ADR-006] Object Pooling for High-Frequency Entities
- **Status**: Accepted
- **Context**: In an FPS, entities like bullets, particle effects, and decals are created and destroyed hundreds of times per second. Standard memory allocation and deallocation for these entities trigger heavy Garbage Collection (GC) spikes, resulting in visible frame drops.
- **Decision**: Implement the Object Pooling design pattern for all high-frequency, short-lived game engine entities.
- **Considered Options**:
  - *Option 1: Standard Instantiation and Destruction (Factory pattern only).* Rejected because the continuous memory allocation fragmentation and subsequent GC pauses ruin client performance.
- **Consequences**:
  - *Pros:* Stabilizes the application's memory footprint and completely eliminates frame drops caused by garbage collection during intense combat scenarios.
  - *Cons:* Increases the baseline memory usage of the application. Developers must strictly enforce the resetting of entity states before returning them to the pool to prevent visual/logic bugs.