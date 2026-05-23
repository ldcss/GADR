
# 2. Use libpcap and libnet

Date: 2017-09-03

## Status

Superceded by [4. Use sockets](0004-use-sockets.md)

## Context

This project is about learning and debugging IPsec.

Therefore it has to analyse every received IPsec datagram by itself and can't rely on the OS kernel.

Likewise it has to craft every IPsec datagram it will send by itself.

## Decision

Use *libpcap* to receive datagrams and *libnet* to send datagrams by the IPsec translator.

## Consequences

The program will be as portable as *libpcap* and *libnet*.

It is easier to store PCAP files in the data store for manual analysis.

