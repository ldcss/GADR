# Software Stack (Core Services)

## Context

As DOS will be an important component of our collections platform,
the software stack (web server, application container, programming language, database)
DOS uses to realize core functionality and to fulfill non-functional requirements 
of scalability, performance, reliability, security, and backward compatibility needs to be robust. Java can help meet various implicit non-functional requirements out of the box. Similarly, the use of proven and
mature ecosystem libraries can help meet the functional requirements easily. The Spring 
framework also makes it relatively easy to create RESTful web services.

## Decision

The core service will rely on Java and Spring framework as the basic stack for implementing core services. 
 

## Status

Accepted

## Consequences

As most DLS engineers are not proficient in Java or JVM languages, information sessions or training may need to be provided to other team members so that they can assist the team in future or as necessary.  Therefore, in addition to extensive documentation, the project team intends to train additional non-DOS developers when we have the capacity in DLS.