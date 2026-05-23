# :bulb: Which API model to use for Cosmos DB

:calendar: Date: 2/10/2020

## :heavy_check_mark: Status : Accepted

## :dart: Context

Azure Cosmos DB provides different APIs to access and interact with the data it stores.

* Core(SQL) API
* Mongo DB API
* Cassandra API
* Azure Table
* Gremlin (graph) API

Choosing the right API model will play a role in integration complexity and data access performance. 

## :traffic_light: Decision

The recommended approach is to use Core(SQL) APIs.

The decision is based on the guidance provided by Microsoft here: https://docs.microsoft.com/en-us/learn/modules/choose-api-for-cosmos-db/3-analyze-the-decision-criteria

## :trophy: Consequences

Ability to use SQL-like querying language. 