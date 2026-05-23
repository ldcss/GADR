# :bulb: Which hosting model to use for Cosmos DB

:calendar: Date: 2/10/2020

## :heavy_check_mark: Status : Accepted

## :dart: Context

Azure Cosmos DB is available in two different capacity modes: provisioned throughput and server less.

Choosing the right model will help optimize the cost and performance

## :traffic_light: Decision

The recommended approach is to use Server less mode

The decision is based on the guidance provided by Microsoft here: https://docs.microsoft.com/en-us/azure/cosmos-db/throughput-serverless 

The approach is based on the following assumptions
* The application had no organizational constraints to use preview technology.
* The application does not have requirements for being geo-redundant. 
* Maximum throughput is less than 5,000 RU/s
* Maximum storage is less than 50 GB

## :trophy: Consequences

Ability to optimize cost by using a pay per use model which is billed per hour. 