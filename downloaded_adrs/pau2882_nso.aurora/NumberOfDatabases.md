# Title

Number of databases required

## Status

accepted

## Context

The state and data are required for the following components: Inventory, Customer, Order Management, Rating Manager and Recommendation Manager.  We had a database for each of the component initially.  However, it can save on the number of distrubted transactions by storing state and data in one database.

## Decision

It was agreed that one database would be sufficient.  

## Consequences

None.  
