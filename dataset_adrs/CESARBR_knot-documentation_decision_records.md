# Architecture Decision Records

Architecture Decision Records (ADRs or simply decision records) are a collection of records for "architecturally significant" decisions. A decision record is a short markdown file in a specific light-weight format.

This folder contains all the decisions we have recorded in KNoT.

## KNoT decision record organization and index
All decisions are categorized in the following folders:
* **Architecture** - Decisions on general architecture, code structure, coding conventions and common practices.

    - [ARC-001: Fog Architecture: Stage 1](./architecture/ARC-001-fog-architecture-stage-1.md)
    - [ARC-002: Fog-Cloud Sync](./architecture/ARC-002-fog-cloud-sync.md)
    - [ARC-003: AMQP Exchange name](./architecture/ARC-003-amqp-exc-name.md)

* **API** - Decisions on KNoT API designs.

* **SDKs** - Decisions on KNoT SDKs.

* **Engineering** - Decisions on Engineering practices, including CI/CD, testings and releases.

## Creating new decision records
A new decision record should be a _.md_ file named as
```
<category prefix>-<sequence number in category>-<descriptive title>.md
```
|Category|Prefix|
|----|----|
|Architecture|ARC|
|API|API|
|SDKs|SDK|
|Engineering|ENG|

A decision record should contain the following fields:

* **Status** - can be "proposed", "accepted", "implemented", or "rejected".
* **Context** - the context of the design discussion.
* **Decision** - Description of the decision.
* **Consequences** - what impacts this decision may create.
* **Implementation** - when a decision is implemented, the corresponding doc should be updated with the following information (when applicable):
  * Release version
  * Associated test cases