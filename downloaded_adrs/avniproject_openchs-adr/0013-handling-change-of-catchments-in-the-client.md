# 13. Handling change of catchments in the client

Date: 2018-06-05

## Status

Accepted

## Context

A change in catchment in a device can be caused by two reasons. 
1. The user-catchment assignment has changed in the server
2. A new user has logged in. 

In both these conditions, 
 - It is possible that there is unsynced data in the device
 - The new user might not have control over old data

A new catchment means that the last update date times are wrong, and the data is also wrong on the device, so this means a full sync from the server. We should do this, but not allow existing unsynced data to be wiped out. 

Also note that the catchment an individual belongs to is set when he/she is created. Therefore, a sync of data will not affect any unsynced data. 

## Decision

When a change in catchment is detected by openchs-client, existing unsynced data will be synced to the server, all data deleted, and a fresh sync started. 

## Consequences

If a user needs to discard existing unsynced data on the client, he/she needs to remove them manually. 
