# 35. All communication uses SSL

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

## Context

Encryption of communication is used to ensure that only the intented recipient can read the information. Even when communication is intercepted, the information will still be protected by the encryption. SSL is a widely used protocol to secure communication over Internet protocols (tcp/ip).

## Decision

We will secure all communication using SSL.

## Consequences

The safe communication that is the result from encryption, comes with additional cost of implemention and management. However, many products nowadays feature easily configurable encryption functionality, which greatly reduces these costs. Next tot that, encryption is a requirement by policies and regulations for some sensitive types of information.
