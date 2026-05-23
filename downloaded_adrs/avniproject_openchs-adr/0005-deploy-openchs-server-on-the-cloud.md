# 5. Deploy openchs-server on the cloud

Date: 2018-05-16

## Status

Accepted

## Context

1. Cost - Most users of OpenCHS are NGOs having 5-10 health workers. A running postgres instance and a tomcat server per installation is hard to support/maintain. 
2. Availability of internet - While users might not have internet connectivity in the field, they are usually attached to a head office where there is internet connectivity. They usually come to this common location regularly. Since sync is the only reason for internet connectivity, it can be limited during these visits. 
3. Future direction - 3g/4g is getting more common across the country, and cloud-based solutions are also getting more pervasive. 

## Decision

Openchs server will have capabilities to be deployed on the cloud

## Consequences

 - We will need to build multitenancy on the server
 - Backward compatibility of APIs on the server will need to be built
