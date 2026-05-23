# [ADR-004] Use UDP for Core Game Network Layer

**Date:** 2026-05-22

## Status
Accepted

## Context
We are developing a 10v10 competitive online FPS game that relies heavily on real-time state synchronization. In fast-paced multiplayer architectures, transient game state data (such as player positioning and inputs) becomes instantly obsolete when a newer state is generated. Achieving minimal latency is critical to support gameplay patterns like client-side prediction, lag compensation, and server reconciliation. We must select a transport layer protocol capable of continuous, high-speed data transmission without introducing artificial bottlenecks during network degradation.

## Decision
The network layer will use the User Datagram Protocol (UDP) to prioritize continuous packet transmission over guaranteed delivery. 

## Considered Options
*   **UDP (Selected):** A connectionless protocol with minimal overhead. It prioritizes transmission speed over reliability, ignoring error checking and packet re-transmission.
*   **TCP (Rejected):** While TCP ensures guaranteed, ordered delivery, its requirement to re-transmit lost packets causes head-of-line blocking. This introduces unacceptable latency spikes ("freezes" or "stutters") that break real-time FPS gameplay.

## Consequences

**Positive:**
*   **Maximum Transmission Speed:** The lack of error checking keeps the protocol lightweight, ensuring the fastest possible delivery of game state updates.
*   **Consistent Latency:** Avoids the compounding delay of packet re-transmissions, which is critical for maintaining a continuous data stream.
*   **Lower Overhead:** Reduces bandwidth usage and processing cost per packet, easily supporting 20 players per match exchanging high-frequency updates.

**Negative:**
*   **No Guaranteed Delivery:** Packets will inevitably be dropped, delayed, or arrive out of order during network congestion.
*   **Increased Application Complexity:** The application layer must handle packet loss independently. Developers must implement entity interpolation, client-side prediction, and server reconciliation to smooth out the player experience when data is missing.