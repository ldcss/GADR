
# 3. Only work with configured VPNs

Date: 2017-09-04

## Status

Accepted

## Context

This system needs storage in the data store for every VPN it deals with.

Since it shall be used to analyse IPsec tunnels it could create the needed storage on the fly when interesting traffic reaches the system.
This would make it easier to get started with a new VPN but it would make the system vulnerable to resource exhaustion.
Additionally it could be triggered with spoofed source addresses to send traffic to arbitrary systems.

## Decision

For every VPN gateway that this system shall interact with, at least the storage in the data store has to be initialized.

## Consequences

The system won't react to IPsec traffic from unknown addresses.

