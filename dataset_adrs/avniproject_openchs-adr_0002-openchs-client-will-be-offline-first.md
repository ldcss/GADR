# 2. openchs-client will be offline-first

Date: 2018-05-16

## Status

Accepted

## Context

OpenCHS client will be used in places of low or no connectivity. This means the application should be usable at any point in time without internet. However, data needs to be pushed to a central server for reporting, as well as for backup. This means no functionality other than sync to server should require connectivity to the server. 

## Decision

OpenCHS client should be usable offline. 


## Consequences

  - The client cannot be used by a group of people in places of no connectivity
  - Login takes place only when there is connectivity
