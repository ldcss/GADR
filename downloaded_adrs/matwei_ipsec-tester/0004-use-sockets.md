# 4. Use sockets

Date: 2020-04-20

## Status

Accepted

Supercedes [2. Use libpcap and libnet](0002-use-libpcap-and-libnet.md)

## Context

The IP stack automatically handles UDP and IP datagrams
when there is no service listening for the port or protocol
by sending ICMP type 3 messages to the sender.

This would interfere with the IPsec exhange
unless there is a process listening
für UDP port 500 or 4500 and for ESP or AH.

## Decision

The program uses sockets for network access.

## Consequences

Libpcap and libnet aren't needed.

