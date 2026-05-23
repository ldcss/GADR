# [ADR-001] Use a Python Simulator for Real-Time Environmental and Traffic Data

**Date:** 2026-05-22

## Status
Accepted

## Context
The system consists of an event-driven agent architecture designed for logistics optimization and real-time urban mobility. Specialized agents (traffic, weather, cost) require a continuous stream of real-time environmental data (e.g., accidents, weather conditions, traffic patterns) to validate routes and make autonomous decisions. 

Relying on external production-grade services (like Google Maps or Waze APIs) introduces prohibitive financial costs, strict rate limits, and integration complexity. Furthermore, since the primary goal of the current phase is to validate the architectural pipeline, agent orchestration, and downstream API consumption, real-world data accuracy is not strictly required. We need a reliable, cost-effective method to artificially generate structured telemetry and environmental data to test system capabilities.

## Decision
We will develop a Python script to periodically simulate and broadcast real-time environmental data and vehicle movement. 

The simulator will randomly generate complex, structured JSON payloads (containing geolocation coordinates, temperature, precipitation, traffic density, and incidents) at regular intervals (e.g., every 5 minutes). These payloads will be published to our message broker, where downstream specialized agents will consume and react to them asynchronously.

## Considered Options
*   **Commercial APIs (Google Maps, Waze, etc.):** Rejected. The financial cost is prohibitive for an MVP/simulation phase, and managing rate limits adds unnecessary operational overhead.
*   **Free/Open-Source Data APIs:** Rejected. Free alternatives often provide unreliable uptime, lack the comprehensive multi-modal data required (e.g., combining traffic, weather, and transit delays), or supply low-quality data.

## Consequences
### Pros
*   **Zero External Costs:** Eliminates the need to pay for premium location and weather API tiers.
*   **Total Test Control:** Allows deliberate injection of critical edge cases (e.g., sudden severe weather or road accidents) to validate the agents' dynamic recalculation capabilities.
*   **Development Speed:** Python’s highly mature data ecosystem makes it trivial to manipulate data, generate complex mock JSON payloads, and interface directly with the message broker.

### Cons
*   **Synthetic Data:** The system will operate on mocked data, meaning real-world predictive accuracy cannot be validated until real APIs are integrated in the future.
*   **Maintenance Overhead:** The team must invest initial development effort to build and maintain the simulation logic, ensuring the generated payloads structurally match what real production APIs would eventually return.