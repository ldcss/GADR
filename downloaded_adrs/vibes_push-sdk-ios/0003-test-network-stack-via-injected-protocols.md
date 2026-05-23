# 3. Test Network Stack via Injected Protocols

Date: 2017-06-06

## Status

Accepted

## Context

There are [two main ways to go about testing your networking stack][2]: 

1. introduce protocols that wrap Apple foundation types (like `URLSession`,
   `URLSessionDataTask`, etc.)
2. introduce a stubbing library like [OHHTTPStubs][1] that leverage
   `URLProtocol` and a small bit of swizzling to allow using JSON fixture data

## Decision

While there are cases where both approaches are appropriate (even in the same
project), we've decided to opt for option 1 (protocol-based testing) of our
networking layer. This allows a more unit-based approach to testing.

## Consequences

Unit testing is fast (and not dependent on the network), which is great most of
the time. Because we also like the assurance of an end-to-end test, we've opted
to include at and Integration test suite that _actually hits the network_ as a
separate Target. This can be run from Xcode, or potentially from CI in the
future.

[1]: https://github.com/AliSoftware/OHHTTPStubs
[2]: https://fatalerror.fm/episodes/2017/2/13/17-testing-your-network-layer
