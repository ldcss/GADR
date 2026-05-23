# [ADR-001] Simulated Environment Data Source via Python Script
- **Status**: Accepted
- **Context**: The urban mobility system requires continuous, real-time data inputs (traffic conditions, weather, road accidents) to feed specialized decision-making agents. Commercial routing and mapping APIs (e.g., Google Maps, Waze) are cost-prohibitive for the current project scope, and free alternatives lack the required data quality and availability to effectively test the orchestration logic.
- **Decision**: Implement a standalone Python script to act as a mock data provider. This script will periodically (e.g., every 5 minutes) generate randomized environmental and traffic events and inject them into the system. 
- **Considered Options**:
  - *Option 1: Integrate with commercial APIs (Google Maps, Waze).* Rejected due to budget constraints and unnecessary financial overhead for a simulation/MVP phase.
  - *Option 2: Use free/open-source location APIs.* Rejected because the data quality, rate limits, and reliability are insufficient to consistently trigger the dynamic recalibration behaviors required by the agents.
- **Consequences**:
  - *Pros:* Zero infrastructure/API costs; provides absolute control over edge cases, allowing developers to easily force specific scenarios (e.g., sudden heavy rain or accidents) to validate agent responses.
  - *Cons:* Does not test real-world integration challenges (network latency, authentic payload parsing, API rate limiting); will require writing a new adapter layer if the system ever migrates to live production APIs.