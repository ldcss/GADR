# Use a cloud service provider to host Traffic Processing Center

* Status: accepted

## Context and Problem Statement

Processing center should be hosted. Where to host it?

## Considered Options

* Use servers located close to sensors and video cameras
* **Use a cloud service provider to host Traffic Processing Center**
* Use on-premise data center

## Rationale
Putting servers close to sensors and video cameras is good due to it allows establishing reliable wired connections to gather all data for processing without losses. But this option has disadvantages: connection to a remote server for service disruption troubleshooting is challenging. The service increases the power supply requirements. Some rules should be applied or cameras at distance (e.g. to measure the average speed between two checkpoints), updates delivery is challenging.

Decision-making service requires raw data. Keeping it remote requires transferring raw data from the point of installation to the service. The total required throughput will be [0.35 Mbps](../figures.md). That's expected to be acceptable.

Even though using an on-premise data center might result in cost savings, a data center is not a product differentiator. Meanwhile, it requires additional operational and implementation efforts. It’s easier to focus on product value and rely on a cloud service provider.

## Feedback
This decision implies that cloud managed services are more preferable to on-premise hosted ones.
