# :bulb: What architecture style to use for the application

:calendar: Date: 2/10/2020

## :heavy_check_mark: Status : Accepted

## :dart: Context

Following Architecture styles were considered for the application
1. n-tier
1. Web-Queue-Worker
1. Microservices
1. Big data/compute

Choosing the right Architecture style will impact the functional and non-functional efficiencies of the project.

## :traffic_light: Decision

A simple Microservices based architecture style was implementing CQS pattern will be used for this application. More about CQS pattern can be found here :https://martinfowler.com/bliki/CommandQuerySeparation.html

The decision is based on the guidance provided by Microsoft here: https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
## :trophy: Consequences

Agility in terms of development speed and deployment will be achieved by adopting this architecture style.