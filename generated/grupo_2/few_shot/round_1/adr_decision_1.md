# [ADR-001] Simulated Data Generation for Environment Variables
- **Status**: Accepted
- **Context**: The logistics and urban mobility system requires continuous real-time data regarding weather, traffic, and transit events to feed specialized routing agents. Integrating real-world external APIs (e.g., Google Maps, Waze) introduces prohibitive costs and restrictive rate limits that hinder the development of this architectural proof-of-concept.
- **Decision**: Implement a standalone Python script to periodically generate and publish randomized, simulated environment data (e.g., weather updates, traffic accidents) instead of consuming live third-party APIs.
- **Considered Options**:
  - *Option 1: Integrate live third-party APIs using a Facade pattern.* Rejected due to the high financial cost of reliable geolocation/traffic APIs and the severe limitations of free alternatives.
  - *Option 2: Build a custom Python-based data simulator.* Accepted as it provides full control over data generation and perfectly fits the testing and simulation scope of the project.
- **Consequences**:
  - *Pros:* Eliminates financial costs and API rate-limit bottlenecks; provides the ability to manually trigger specific edge cases (e.g., sudden roadblocks) to test agent responsiveness and system resilience.
  - *Cons:* The system will operate on artificial data, requiring a data-layer refactor to integrate actual APIs if the project ever transitions to a production-ready real-world application.