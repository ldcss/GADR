# :bulb: Which compute service to choose for the serving tier of the application

:calendar: Date: 2/10/2020

## :heavy_check_mark: Status : Accepted

## :dart: Context

Azure offers a number of ways to host your application code. The following are the considerations for choosing a compute option for the serving tier:

* Should support exposing Web APIs
* Should be able to connect to backend Cosmos DB
* Should support .net core framework
* APIs hosted on this service will need to be secured
* Would prefer a managed service
* Does not have portability requirements
* Should support CD from Github

The following options for compute are considered for this service:
* App Services
* Functions
* Container Instances
* Service Fabric
* AKS

Choosing the right compute model will help optimize the development experience and operations

## :traffic_light: Decision

The recommended approach is to use Azure App Services considering the following points:
* Supports CD from Github
* Supports development slots for updates to reduce downtime
* Can be integrated with App Gateway and VNET for higher security
* Natively supports AD integration
* Supports .net core framework and is well integrated with Visual Studio development experience
* Can leverage cosmos SDK (nuget) to connect back to the data store
* Is a fully managed PaaS service
* No overheads related to cluster management or infrastructure provisioning.

The decision is based on the guidance provided by Microsoft here: https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree


## :trophy: Consequences

Azure App Services will optimize the operation cost and enhance the development experience for the team