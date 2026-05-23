# Evaluate Spring Data REST

Technical Story: [Evaluate Spring data rest](https://github.com/UST-MICO/mico/issues/83)

## Context and Problem Statement

We want to use CRUD operations to manipulate our domain model.
Furthermore, we don't want to write REST controllers if it is not necessary.

## Decision Drivers

* Must allow CRUD operations
* It must be possible to extend the API and to add resources or sub resources which are not managed by Neo4j
* It must be compatible with Springfox
* The API must be RESTful

## Considered Options

* Spring Data REST
* Manually writing Spring REST controllers (based on Spring HATEOAS)

## Decision Outcome

Chosen option: Spring Data REST, because it automatically exposes or domain model and so we don't have to write the required rest controllers our self. In addition to that paging, sorting and the HAL media type are supported out-of-the-box. Extending or overwriting Spring Data REST Response Handler is also possible and allows us to add custom logic if needed [[1]].

## Pros and Cons of the Options

### Spring Data Rest

* Good, because our model is exposed automatically
* Good, because it supports paging, sorting and HAL
* Good, because changes in the model are automatically reflected in the API
* Bad, because we have to use a nonstable version of Springfox (3.0.0-SNAPSHOT) [[2]]
* Bad, because we need to tweak the generated API to map some features of our domain model nicely (e.g. service1->dependsOn->service2->...)

### Manuel approach

* Good, because we have more control over the resources which are offered be our API
* Good, because it is easier to hide internal changes to offer a more stable API
* Bad, because it requires more manual work

[1]: https://docs.spring.io/spring-data/rest/docs/current/reference/html/#customizing-sdr.overriding-sdr-response-handlers
[2]: https://github.com/springfox/springfox/issues/1957
