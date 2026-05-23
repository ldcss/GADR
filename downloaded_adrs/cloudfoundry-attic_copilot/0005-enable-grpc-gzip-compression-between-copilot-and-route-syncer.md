# 5. Enable GRPC GZIP compression between Copilot and Route Syncer

Date: 2018-11-07

## Status

Accepted

## Context

The GRPC default message size of 4 mb currently causing a bottleneck between cc-route-syncer and copilot. As our message sizes increased with scale this prevents us from sending messages to copilot.

## Decision

We have decided to reduce the message size by enabling GRPC's GZIP compression between cc-route-syncer and copilot.

## Consequences

This could be potentially a temporary fix as the message size gets bigger. The GZIP compression message size could still go above the default message size in GRPC in the future.

## Update (2018-11-14)

After implementing the gzip compression, our bottleneck was not resolved. It turns out that the error message we are encountering [captures the length of the message size _after_ it is decompressed](https://github.com/grpc/grpc-go/blob/v1.15.0/server.go#L947-L966). We are keeping the gzip compression in place as we don't expect there to be much of a drawback for it but we can revisit this in the future if issues arise.
