# 7. feat-code-for-microservices-arch

Date: 2020-02-20

## Status

Accepted

## Context

Goals:

* Use a set of microservices to deploy to the platform

I have invested some time to learn about microservices as I was not very
conscious about what implies today and what is different between languages.

I have coded Python and Springboot apps to see which one will give me better
fit in my example here.

Spring has several components to create microservices that can be really
 useful, like:

- eureka server: as discovery server
- eureka client: a library for self-registering into eureka server
- feing rest client: a powerful but simple REST client
- zuul gateway: a reverse proxy application that performs as api gateway
- config server: a configuration management server for spring cloud apps.


## Decision

I have added a small set of SpringBoot microservices to help me work on the
 test.

This example creates 4 small microservices:

* servicio-productos: models a product and provides a REST interface
* servicio-items: consume products, ask for quantities and models an item, exposes data as REST interface
* servicio-eureka-server: discovery service from netflix where all apps can self-register and find for other services addresses.
* servicio-zuul-server: a reverse-proxy to access the item and product APIs in a common way.
* servicio-config-server: a configuration management server configured against a git
 repository to set the variables used by the applications.


## Consequences

I have spent a lot of time on this, but I have a clear view about how this
 architecture works, and how could I scalate.
