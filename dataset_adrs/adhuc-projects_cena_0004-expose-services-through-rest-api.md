# 4. Expose services through REST API

Date: 2018-12-27

## Status

Accepted

## Context

`menu-generation` application needs to expose data and services in order to be used by multiple different applications,
either web or mobile front-ends or any other application that will reuse a sub-part of the `menu-generation`
application or enhance the provided services.

We want the application data and services to be easily consumed through well established communication protocols, such
as HTTP. It must be intuitive to manipulate the `menu-generation` application as a self-discoverable API, without
managing cumbersome protocols or data formats.

## Decision

`menu-generation` application data and services will be exposed through a REST API.

## Consequences

REST is an architectural style that expose resources as an API to consumers. This architectural style involves many
constraints:

* adopting a **client-server architecture** that promotes separation of concerns. It improves scalability by simplifying
the server components, reusability of the server features by multiple clients, and allows clients and servers to evolve
independently.

* allowing **layered system** between the client who requests a representation of a resource’s state and the server who
sends the response back. Layered system can provide a number of features (e.g. security, caching, load-balancing). Those
layers should not affect the request or the response. The client is agnostic as to how many layers, if any, there are
between the client and the actual server responding to the request.

* enforcing **stateless** communication, so that each request from client to server must contain all of the information
necessary to understand the request, and cannot take advantage of any stored context on the server. Session state
(e.g. authenticated user) is therefore kept entirely by the client.

* enabling **cacheable** content, meaning that the data within a response to a request be implicitly or explicitly
labeled as cacheable or non-cacheable. If a response is cacheable, then a client cache is given the right to reuse that
response data for later, equivalent requests.

* exposing a **uniform interface**, through:
    * identification of resources
    * manipulation of resources through representations
    * self-descriptive messages
    * hypermedia as the engine of application state

`menu-generation` application architecture will embrace all those constraints. It means that:

* the API will be based on the HTTP protocol as an application layer, using the protocol semantics.

* REST adapters will expose API resources through representations that will be decorrelated from aggregates as defined
by the domain model.

* each resource will contain at least its own resource identifier in the form of a link included in the representation.

* every service in the application will be stateless, state being stored through the repositories in the underlying
persistence technology.
