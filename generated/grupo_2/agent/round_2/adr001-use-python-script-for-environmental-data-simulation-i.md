# [ADR-001] Use Python Script for Environmental Data Simulation Instead of Facade Pattern for External APIs

**Date:** 2026-05-22

## Status
Accepted

## Context
Our agency architecture focuses on real-time logistics optimization and urban mobility, requiring external environmental data (weather, traffic, accidents) to allow specialized agents to calculate and coordinate multimodal routes asynchronously. Initially, integrating with real-world mapping and weather APIs (e.g., Waze, Google Maps) via a Facade design pattern was considered to manage subsystem complexity. However, reliable real-world APIs are prohibitively expensive or severely rate-limited. Furthermore, the core objective of this project is validating the event-driven architecture (EDA) and agent orchestration logic, not real-world data integration.

## Decision
We will use a standalone Python script to periodically simulate and generate mock environmental data instead of implementing a Facade pattern to integrate with external mapping APIs. This script will run at defined intervals (e.g., every 5 minutes), generate complex JSON payloads containing relevant metrics (coordinates, timestamps/epochs, temperature, traffic density), and publish them directly to our message broker for agent consumption.

## Considered Options
*   **Python Mock Data Generator Script (Chosen):** Generates randomized, targeted environmental events pushed directly to the broker. Aligns with the project's simulation constraints and asynchronous architecture.
*   **Facade Pattern for Real-World APIs (Rejected):** Utilizing a single-class or subsystem Facade to wrap external APIs would abstract integration complexity. Rejected because securing the necessary third-party API access is expensive, difficult, and unnecessary for demonstrating the core MVP architecture.
*   **FastAPI Mock Service (Rejected):** Serving simulated data via a FastAPI REST endpoint. Rejected because our agents operate as consumers in a publish-subscribe event-driven architecture; pushing data to a message queue is more efficient than forcing agents to poll an API.

## Consequences
**Pros:**
*   **Cost-Effective:** Zero financial cost associated with third-party API subscriptions.
*   **Scenario Control:** Complete control over data payloads, making it easier to trigger edge-case scenarios (e.g., sudden accidents, extreme weather) to test agent recalculation logic.
*   **Reduced Architectural Complexity:** Eliminates external network dependencies and circumvents the need to debate OOP vs. FP paradigms required to properly implement a structural Facade pattern.

**Cons:**
*   **Maintenance Overhead:** The team must build and maintain the Python generation script, ensuring it accurately produces the complex, nested JSON payloads required by the agents.
*   **Lack of Fidelity:** Simulated data may not perfectly replicate the nuance and unpredictability of real-world urban mobility events.