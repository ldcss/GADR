# ETL and CDH Communication ADR


## Status

Accepted

## Context

We wish to segment into separate processes where the data feed files processing is handled by the ETL service and the CDH service is reponsible for consuming these produced output which then are materialized into records which is used in response to request to the CDH service. This means ETL service must be able to communicate to the CDH service loosely without direct connection or dependence between either. 

## Decision

We have chosen an event based communication where the CDH and ETL service communicate results between each other over an event queue based on specified topics (deployed onsite within geozone of CDH and ETL services). 

![Event Queue](../assets/images/workflows/image3.png)

## Consequences

We must deploy a selected (currently Solace) event queue with a specified event topic(s) which will be responsible for 
housing specific events which will be used by CDH for ETL results for processing.