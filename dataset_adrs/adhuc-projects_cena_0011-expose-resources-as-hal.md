# 11. Expose resources as HAL

Date: 2019-02-11

## Status

Accepted

## Context

`menu-generation` application will expose its data and services through a [REST API](0004-expose-services-through-rest-api.md).
One of the constraints of the REST architectural style implies exposing **Hyperlinks as the Engine of Application State**,
meaning any resource should provide links to other accessible resources based on its current state in the application,
so that clients can discover which actions are available without interpreting the actual resource attributes.

[Spring HATEOAS](https://spring.io/projects/spring-hateoas) comes by default with [HAL](http://stateless.co/hal_specification.html)
media type support.

## Decision

`menu-generation` application will expose its resources using the HAL media type.

## Consequences

Based on the HTTP content negotiation, `menu-generation` application API will accept and return either HAL
(i.e. `application/hal+json`) or plain JSON (i.e. `application/json`) media types, favoring HAL when both are acceptable,
as HAL is a specification based on JSON structure, thus fully compliant with plain JSON.

Resources representations will be compliant with HAL specification.

Further media types may be supported in the future.
