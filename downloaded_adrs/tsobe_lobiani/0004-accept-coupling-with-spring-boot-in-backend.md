# 4. Accept coupling with Spring Boot in backend

Date: 2021-01-09

## Status

Accepted

Also see [8. Use AxonFramework in backend](0008-use-axonframework-in-backend.md)

## Context

Almost every software project needs to interact with the 3rd party libraries and frameworks to some extent. 
Generally, the less coupled the code is with the 3rd party libraries and frameworks (usually thanks to additional abstraction 
layers on top of them), more flexible the software becomes in regard to technology replacements in the future.

However, sometimes it's quite viable to compromise this flexibility in favor of practical benefits that particular
technology brings, in this case Spring Boot/Framework. Especially that it is designed with the abstraction and 
extensibility in mind, so introducing another layer of abstraction is senseless.


## Decision

We accept direct coupling with Spring Boot/Framework code without any abstraction layers on top of it.

## Consequences

- We will focus more on the problems specific to our domain, thanks to the fact that most of the non-domain-specific 
problems are already solved by Spring Boot/Framework and integrated projects
- Code will be locked in with the Spring Boot/Framework. It will require significant efforts to port the code to different 
technologies if we change our minds in the future for some reason
