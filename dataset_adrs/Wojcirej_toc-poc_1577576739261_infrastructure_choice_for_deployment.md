# Infrastructure choice for deployment
## Added at: 2019-12-28 23:45:39 UTC
## Status: Accepted

## Context
The final effect of the POC will be static HTML page, with css and javascripts included in the file. Therefore, it will be easy to host it online for demonstration purposes, with configuration for multiple environments.

## Decision
Use S3 static webpage hosting as deployment infrastructure.

## Consequences
### Positive
* Really quick preparation of such infrastructure.
* Setup can be automated easily with not much effort with SDK as well.
* Does not require complicated configuration.
* Deployment can be solved easily within application service, considering architecture choice and it's configurability (repository design pattern used for HTML storage).
### Negative

## Other options
* EC Instance with Apache HTTP Server - bit more complicated to setup (opening ports, installation of the server service) and I don't have knowledge about automation of this kind of infrastructure yet. Also, smells like a bit overkill for one HTML file.
