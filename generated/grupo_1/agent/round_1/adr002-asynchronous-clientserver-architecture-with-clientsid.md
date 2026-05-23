# [ADR-002] Asynchronous Client-Server Architecture with Client-Side Prediction and Server Reconciliation

**Date:** 2026-05-11

## Status
Accepted

## Context
We are developing a 10v10 competitive online FPS game. Network latency inherently delays communication between clients and the server. Waiting for server confirmation before rendering player actions (strict synchronous execution) introduces unacceptable input lag, degrading the fast-paced gameplay experience. We require a network synchronization strategy that masks latency, guarantees authoritative state management to prevent cheating, and provides users with a smooth, seemingly synchronous experience despite underlying asynchronous data streams.

## Decision
We will implement an asynchronous client-server architecture utilizing mini-buffers, client-side prediction, and server reconciliation. 

Specifically:
* **Client-Side Prediction:** The client will immediately simulate the expected outcome of local inputs without waiting for asynchronous server confirmation.
* **Mini-Buffers:** The client will store recent local inputs and their resulting simulated states in a local prediction buffer indexed by the current simulation tick.
* **Server Reconciliation:** The server remains the sole authority. The client will continuously compare its buffered predicted state against the authoritative state snapshots received asynchronously from the server.
* **State Correction (Rewind/Replay):** Upon detecting desynchronization, the client will unconditionally roll back to the server's authoritative state, then invisibly rewind and replay the remaining unprocessed inputs from the mini-buffer to seamlessly correct the present local state.

## Considered Options
* **Strict Synchronous Architecture (Lockstep):** Rejected. Waiting for network round-trips before rendering inputs causes severe, visible input lag, which is unacceptable for a competitive FPS.
* **Peer-to-Peer (P2P) Architecture:** Rejected. P2P lacks a centralized authoritative state, making it highly susceptible to cheating, host advantage, and complex state desynchronization across 20 distinct players.

## Consequences

**Pros:**
* **Illusion of Synchronicity:** Effectively masks network latency, yielding a highly responsive experience where input feels immediate.
* **Competitive Integrity:** The server retains absolute authority over the game state, preventing clients from manipulating their position or actions.
* **Smooth Rendering:** Interpolation and prediction mini-buffers prevent micro-stutters during standard packet delivery variance.

**Cons:**
* **Increased System Complexity:** Requires sophisticated client logic to manage input buffering, state snapshots, and seamless rewind/replay loops.
* **Rubber-Banding Risks:** Under extreme latency or packet loss, the divergence between predicted and authoritative states will cause abrupt, visible position corrections (rubber-banding/freezing).
* **Higher Processing Overhead:** Both client (re-simulating past inputs) and server (lag compensation, hitscan validation, and snapshot generation) face increased CPU loads compared to naive network models.