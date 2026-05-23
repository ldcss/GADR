# 4. Use local data for Tower Hamlets CCG

Date: 2018-10-02

## Status

Accepted

## Context

Tower Hamlets CCG's IAPT service does not have an ODS code. As a consequence it
is not possible to relate the CCG to the IAPT service. When a GP is providing
services for Tower Hamlets CCG this will allow data to be displayed.

## Decision

Rather than display no result we know the contact information for the IAPT
service. We have decided to store this information locally and display it for
the user.
This is only a temporary measure and the change will be reverted once the data
has been loaded into the central system.

## Consequences

The data stored locally is not managed centrally, as all other data is.
This change is only temporary and will be reverted once the data has been added
into the central systems.
