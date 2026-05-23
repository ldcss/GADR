# CDH Tenants


## Status

Accepted

## Context

Monolith will undergo segmentation where we plan to pull out the Client Data Hub out of the monolith as a separate service for better scaling and API management. The functionality of the client data hub to provided tenant, transaction and position related data will stay the same, but the data feed parsing within it's perview will also be moved out into an [ETL Service](./etl.md).

The client data hub provides the following services:

1. Delivery of tenant information (Accounts, Company, and Client data).
2. Delivery of Tenant Transaction (Data Feed and Systems) for specified periods of time.
3. Delivery of Tenant Positions for their related transactions for porfolio tracking.
4. Processing of reconciliation request on tenant accounts and positions.

This requires us to consider migration procedures for moving existing data from the monolith into the new CDH and ETL related databases.


## Decision

Create a specific services (ETL and CDH) where an ETL service and CDH service will be responsible for the processing of delivered PriveXML for consumption and delivery of client transactions + positions into data tables. Both services will communicate across a pubsub event bus.

The following is expected:


- CDH will expose an API by which it will handle all tenant and transaction related requests from monolith. 
- CDH will listen on specified event topic on message bus from which all tenant update requests will be received as events
- CDH will publish to the monolith events on updated tenant data by which monolith will update it's records.
- CDH will have all tenant data moved from monolith into it's control (to be discussed in CDH Tech).
- CDH will consume all PriveXML events to update it's records of transactions + tickers + positions.


![CDH Architecture](../assets/images/aab_workshop/aab_5.jpg)

## Migration

We will begin migrating a simple feed for CDH which will have both tenant data + transaction data (Transactions + Positions + Tickers) transformed into PriveXML data
which will then be consumed by new CDH service for populating it's table, this will allow legacy archiving of existing data as PriveXML before moving these into new CDH.

## Consequences

What becomes easier or more difficult to do because of this change?