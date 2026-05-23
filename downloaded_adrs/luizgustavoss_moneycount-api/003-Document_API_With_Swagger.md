# Title: 003 - Document APIs with Swagger


## Status

accepted


## Context

Offer an API without a good documentation is not a choice. Document this API with text documents is not efficient, and as the code changes more and more effort are necessary to keep it up-to-date. It's necessary to document APIs in a simply and efficient way, preferably in a way that developers can test it. 


## Decision

I decided to use Swagger as a documentation tool for the APIs, as it is a de facto standard. I choosed springfox-swagger2 and springfox-swagger-ui because of its smooth integration with Spring Boot.


## Consequences

An easy-to-use and always up-to-date documentation for the end user developer, and an efficient tool to document APIs. Some effort is necessary to have a more detailed documentation, with annotations in methods and attributes in REST controllers, but even without it is possible to have a basic documentation with no code.
