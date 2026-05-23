# [ADR-002] Implement Client-Side Prediction and Server Reconciliation

**Date:** 2026-05-22

## Status
Accepted

## Context
We are developing a competitive 10v10 online First-Person Shooter (FPS). In this architecture, the server must maintain ultimate authority over the game state to prevent cheating and ensure fairness. However, relying purely on a server-authoritative model means clients must wait for a network round-trip to see the results of their inputs. Research indicates that even in environments with incredibly low network latency (as low as 1 ms), this delay causes a noticeably sluggish and unresponsive user experience. To meet the strict responsiveness requirements of an FPS, we must decouple local input rendering from server confirmation without compromising server authority. 

## Decision
The network architecture will implement client-side prediction and server reconciliation over a UDP-based network layer. 

The client will immediately predict and simulate the outcome of local movements and actions to prevent visible lag. Concurrently, the server will process the inputs and broadcast the authoritative state. Upon receiving the server's authoritative state, the client will evaluate it against its local historical state. If discrepancies exist, the client will utilize server reconciliation algorithms to smoothly correct the local state, preventing jarring visual corrections ("backward snapping" or rubber-banding).

## Considered Options
* **Pure Server-Authoritative (Strict Synchronous):** The client waits for server confirmation before rendering any movement. *Rejected* due to introducing unacceptable input lag, rendering the FPS unplayable even under low latency conditions.
* **Client-Authoritative (Peer-to-Peer Trust):** The client calculates its state and the server blindly accepts it. *Rejected* due to severe security risks; it allows trivial cheating (e.g., speed hacks, teleporting) in a competitive environment.

## Consequences

**Pros:**
* **Zero Perceived Latency:** Eliminates visible input lag for the local player, creating a highly responsive gameplay experience.
* **Maintained Integrity:** The server retains absolute authority over the game state, strictly preventing movement and action-based cheats.
* **Network Resilience:** Masks minor network jitter and packet loss effectively from the player's perspective.

**Cons:**
* **Implementation Complexity:** Requires building and maintaining complex client logic to handle historical input buffers, state rewinding, and re-simulation.
* **Risk of State Snapping:** If prediction heavily diverges from the server state, clients will experience jarring backward snapping (rubber-banding). Robust reconciliation and smoothing techniques (interpolation/extrapolation) are required to mitigate this.
* **Server Overhead:** The server must maintain historical state buffers (snapshots) to properly validate delayed client inputs and execute lag compensation.