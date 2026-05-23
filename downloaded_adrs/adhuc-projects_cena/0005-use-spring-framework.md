# 5. Use Spring Framework

Date: 2018-12-27

## Status

Accepted

## Context

[Hexagonal architecture](0003-adopt-hexagonal-architecture.md) requires inversion of control to inject infrastructure
services implementations dependencies into the services defined in the core hexagon.

REST API implementation requires a dedicated library to define incoming adapters handling the HTTP resources.

Spring is a well established framework for Java. It is non-invasive and provides multiple features such as IoC, AOP,
REST services implementation, security that will help speed up implementation in a cohesive way. The author has also used
Spring for many years and masters many of the provided features.

## Decision

Spring framework will be the backbone for `menu-generation` application.

## Consequences

Usage of Spring will include at least IoC, REST services implementation and security. Further requirements may also
require using other parts of the framework, such as Spring Cloud or Spring Data.

Spring Boot will also provide a cohesive approach of the application lifecycle management, using its embedded application
server feature, its bill of materials for dependencies management and its production-ready features.

Spring WebMvc will be preferred to Spring WebFlux to implement the REST services.

Aggregate packages must not depend on Spring framework.
