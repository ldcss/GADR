# :bulb: Which compute service to choose for Ingestion sub-system

:calendar: Date: 2/10/2020

## :heavy_check_mark: Status : Accepted

## :dart: Context

Azure offers a number of ways to host your application code. The following are the considerations for choosing a compute option for the ingestion sub-system:

* Should support scheduling
* Should support running in background
* Should be able to connect to backend Cosmos DB
* Should support .net core framework
* Service will only run once a day
* Would prefer a managed service
* Does not have portability requirements

The following options for compute are considered for this service:
* App Services
* Functions
* Container Instances
* Service Fabric
* AKS

Choosing the right compute model will help optimize the development experience and operations

## :traffic_light: Decision

The recommended approach is to use Azure Functions considering the following points:
* Supports consumption plan (Pay-per-use) which is ideal for sparse usage
* Supports .net core framework and is well integrated with Visual Studio development experience
* Can leverage cosmos SDK (nuget) to connect back to the data store
* Has built-in scheduling capabilities
* Is a fully managed PaaS service
* No overheads related to cluster management or infrastructure provisioning.

The decision is based on the guidance provided by Microsoft here: https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree


## :trophy: Consequences

Azure functions will optimize the operation cost and enhance the development experience for the team