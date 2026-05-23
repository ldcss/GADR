# 3. High Level Infrastructure Design

Date: 2017-07-24

## Status

Accepted

## Context

A just enough high level infrastructure design is needed to drive how we build the strategic infrastructure.

The key questions are;
- How do Application Service Environments (ASEs) fit in the infrastructure?
- What are the IP ranges?
-  What’s the IP allocation policy?
-  How do we handle internal DNS queries?
-  How do the components connect to each other on the network?


## Decision

[High Level Design](https://www.lucidchart.com/documents/edit/69b50fa0-77e7-43b5-92ed-1933abb10a80)

![](../../img/high-level-infra-design.png)

### Production Applications Infrastructure VNet (applications-prod)
Production services will run inside a dedicated Virtual Network (VNet). 

### Management and Tooling Infrastructure VNet (management-prod)
Management and Tooling will be hosted inside a dedicated VNet. This hosts the CI/CD Tooling and components which support  managing and deploying applications. 
 
### Non-Production Applications Infrastructure VNet (applications-non-prod)
Dev, Test (QA) and Load test versions the services will run inside this VNet. The same infrastructure as code (IaC) will drive both prod and non-prod infrastructure.

### Azure Traffic Manager 
[Azure Traffic Manager](https://azure.microsoft.com/en-gb/services/traffic-manager/) will be used to host the public DNS entries for each Citizen facing frontend. 

Traffic Manager supports configurable routing, which will support [blue/green deployments](https://martinfowler.com/bliki/BlueGreenDeployment.html).

### Azure Application Gateway + Web Application Firewall
[Azure Application Gateway](https://docs.microsoft.com/en-us/azure/application-gateway/application-gateway-introduction)

The Azure Application Gateway will be used as a gateway for HTTPS traffic. It will be used to expose internal service for public consumption. 

Services that are not exposed by the Azure App Gateway cannot be accessed externally. 

The Web Application Firewall component of the Azure App Gateway,  comes preconfigured with CRS 3.0 by default or you can choose to use 2.2.9. CRS 3.0 offers reduced false positives over 2.2.9. The ability to customize rules to suit your needs is provided. Some of the common web vulnerabilities which web application firewall protects against includes:

- SQL injection protection
- Cross site scripting protection
- Common Web Attacks Protection such as command injection, HTTP request smuggling, HTTP response splitting, and remote file inclusion attack
- Protection against HTTP protocol violations
- Protection against HTTP protocol anomalies such as missing host user-agent and accept headers
- Prevention against bots, crawlers, and scanners
- Detection of common application misconfigurations (i.e. Apache, IIS, etc.) 


### Azure Application Service Environments with Internal Load balancer

The Application Service Environment provides an isolated and dedicated environment for securely running apps. See [App Service Environment Documentation](https://docs.microsoft.com/en-us/azure/app-service/app-service-environment/readme)

An ASE hosts applications. Each application spans one or more nodes within an ASE. An application uses more nodes according
to it’s scale.

The entry point to applications is via an internal load balancer  (ILB) attached to the ASE. The ILB handles the routing and SSL offload. 



### Private DNS 

A private DNS service will run inside each VNet to provide name resolution for services within the network. 
The DNS solution is TBD.

### TLS/SSL by default

All traffic flows between components will be TLS/SSL enabled. 

## Consequences

TBD 

