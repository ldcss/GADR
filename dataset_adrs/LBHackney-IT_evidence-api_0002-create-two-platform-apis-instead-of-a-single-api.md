# 2. Create two platform APIs instead of a single API

Date: 2020-12-10

## Status

Accepted

## Context

This application was created to allow services to manage gathered evidence documents in a consistent, safe and centralised way. An early decision point was reached with regards to designing the architecture around this capability.

The basic functionalities known to be required are:
- secure storage and management of documents provided by residents and other third parties
- tracking of rights and retention over those documents by the council
- requests and approval of evidence from third parties
- management of evidence requests by officers

Influencing factors:
- HackIT's [API Playbook](https://github.com/LBHackney-IT/API-Playbook-v2-beta)
- [Clean Architecture](https://github.com/madetech/clean-architecture) principles

## Decision

We decided to create two Platform APIs (as defined in the API Playbook):
- A [Documents API](https://github.com/LBHackney-IT/documents-api) for the storage and management of documents and claims over them
- An [Evidence API](https://github.com/LBHackney-IT/evidence-api) for the management of evidence requests and reviews

## Consequences

This has some drawbacks:
- implementation of features across both domains will be more effort and therefore slower
- client requests will have to travel through more applications, introducing longer requests and risks that go along with distributed, asynchronous operations

It also has a number of benefits:
- makes a clear division between the concepts of "evidence" and "documents", which is inline with Hackney's strategy to create Platform APIs which are responsible for a single "kind" of data
- provides a foundation for future needs by other services for centralised storage of documents which are not evidence
- keeps the codebase responsible for managing evidence free from the low level implementation of file and object management

Due to the goals of the project building these capabilities including ensuring the services built are robust, future-proof parts of a wider platform which can be adopted across the council (rather than tactical solutions designed for specific service needs), it was decided these benefits outweight the drawbacks.
