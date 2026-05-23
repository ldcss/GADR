# 3. Use MCP API for Pilot Config

Date: 2018-09-11

## Status

Accepted

## Context

Mesh Configuration Protocol (MCP) is a [protocol](https://github.com/istio/api/tree/master/mcp) for transferring configuration among Istio components during runtime. MCP is meant to defer all the logics and complexities back to the server (copilot) as oppose to the original design which all the logic was embeded in the client (Pilot). Another goal of MCP is to create a unified contract for all the Custom Resource Definitions and Service Discovery and the way they are communicated with Pilot.

## Decision

Copilot will implement a MCP server to send configuration to Pilot. We will be sending definitions for Gateways, VirtualServices and DestinationRules over bi-directional GRPC. 

## Consequences

- All logics around building the configurations will now be in Copilot.
- Logic in Pilot can be removed and pull requests to Istio/Pilot will no longer be necessary.
