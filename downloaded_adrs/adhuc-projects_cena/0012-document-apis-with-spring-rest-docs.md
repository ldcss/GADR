# 12. Document APIs with Spring Rest-Docs

Date: 2019-02-11

## Status

Accepted

## Context

Even a self-discoverable API needs to be documented to let consumers understand the underlying application features and
the resources attributes significance.

A good API documentation will provide requests and responses structure, defining each attribute, giving examples and
mixing functional and technical information so that consumers do not need to traverse different documents to get a
complete overview of the features and technical concerns.

The documentation must also provide links between different parts of the document, so that it is easy to go back and
forth between those parts.

The documentation must be kept in sync with the features. Ideally, a documentation is generated from the code.

## Decision

`menu-generation` will generate its API documentation with [Spring Rest-Docs](https://spring.io/projects/spring-restdocs).

## Consequences

The documentation will be written with `Asciidoctor` format. It will include some snippets generated from the tests.

Some tests must be defined for REST adapters to generate snippets of code. Those tests will help maintaining the
documentation in sync with exposed features, as `Spring Rest-Docs` enforce every part of an API usage to be documented.

Build process must include a phase to generate the documentation. `Spring Rest-Docs` provides a [Gradle](0006-manage-build-with-gradle.md)
plugin to help integration.

The documentation will be exposed directly from the application through a dedicated endpoint.
