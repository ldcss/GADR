# 002 - Shared Database

- Date: 2020/01/02
- Status: Accepted
- Deciders: Daniel Stefaniuk, Matthew Begley, Jonathan Pearce

## Context

This is not an external API to DoS, it is part of the DoS ecosystem. The operation of the API is updating the capacity of services in DoS, for visible in the DoS UI and applications that use Core DoS data.

## Decision

The relevant content of the database is shared between the Core DoS application and the Capacity Status API. The decision was made to have the API use and update the Core DoS database. This approach is the most logical solution at this time, as any other alternative would likely need to incorporate some kind of interim internal API between the Capacity Status API and the Core DoS database. Having an interim API would be replicating functionality of the Capacity Status API and would therefore be redundant.

## Consequences

- The Capacity Status API depends on the Core DoS table structure and is sensitive to any changes in the upstream project (Core DoS).
- In the course of developing the API if there is a need to store additional information. A choice will need to be made about whether to store this information in the DoS database or in a new API specific database.
- The decision to use the DoS database is a pragmatic approach to simplify the architecture, and will be reviewed in the future.
- As a result of this decision a selective copy of the Core DoS database has been created for development purposes, with only the `services`, `servicecapacities`, and `capacitystatuses` tables populated.
