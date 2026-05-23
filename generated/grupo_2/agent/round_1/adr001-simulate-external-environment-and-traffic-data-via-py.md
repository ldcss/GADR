# [ADR-001] Simulate External Environment and Traffic Data via Python Script

**Date:** 2026-05-11

## Status
Accepted

## Context
The system is an event-driven, multi-agent architecture (traffic, cost, weather agents) aimed at logistic optimization and real-time urban mobility. Agents must continuously process and compare transport modes based on dynamic external variables to autonomously recommend optimal routes. Integrating with commercial third-party APIs (like Google Maps, Waze, or specialized weather platforms) is cost-prohibitive for this MVP. Furthermore, free-tier alternatives are highly rate-limited, unreliable, and lack the data quality required to test the real-time, asynchronous orchestration of our system. 

## Considered Options
1. **Commercial Third-Party APIs:** Rejected due to high financial costs unsuitable for our current scope.
2. **Free-Tier/Open APIs:** Rejected due to strict rate limits, low reliability, and poor data granularity, which hinder high-frequency event testing.
3. **Custom Python Simulation Script:** Selected option.

## Decision
We will build a custom Python 3 script to simulate external environmental and traffic data instead of integrating with real third-party APIs. This script will run periodically (e.g., every 5 minutes) to generate randomized but structured situational events (e.g., accidents, weather shifts, subway delays) and publish them to our central message broker. The specialized agents will consume these simulated events to trigger route recalculations.

## Consequences

**Pros:**
* **Zero Cost:** Eliminates the financial overhead associated with location and weather APIs.
* **Controlled Scenario Testing:** Grants complete control over data generation, allowing us to easily force critical edge cases (e.g., severe weather, sudden road closures) to validate agent logic.
* **Ecosystem Alignment:** Aligns with our existing Python foundation (Python 3, FastAPI, SQLAlchemy, Pytest) and supports our strategy of mocking external services during testing.
* **Decoupled Development:** Removes external network dependencies, preventing development bottlenecks related to API keys or downtime.

**Cons:**
* **Development Overhead:** Requires dedicated engineering effort to build and maintain the randomized data generation algorithms.
* **Data Fidelity:** Simulated situations may lack the nuanced complexity and correlated factors of real-world urban mobility.
* **Future Rework:** Transitioning to a production environment later will require replacing the simulation script with actual third-party API integration layers.