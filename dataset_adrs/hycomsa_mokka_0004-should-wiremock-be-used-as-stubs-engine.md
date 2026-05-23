# 4. Should Wiremock be used as stubs engine

Date: 2020-02-10

## Status

Open

## Context

Mokka's stubs engine is required to provide set of new features that will allow better (wider) support of request matching,
(i.e. headers, cookies, variety of patterns), proxying and recording interactions.

It has been considered if further development of Mokka stubs engine should be continued or we should research and adopt one of existing, grown up and production ready solution.

WireMock (http://wiremock.org/) was chosen as one of the most popular mock server with strong and active open source community. It provides consistent and reach API (both: Java and HTTP JSON).
Through years it became one of the mostly chosen library for mocking external services in JUnit tests and also the core part of Spring Cloud Contract library.
By reusing WireMock standards, Mokka may benefit in easier integration with already existing solutions, products and projects.

Table below comparises features of Mokka and WireMock in context of stubbing/mocking engine.
Please mind it does not considers GUI or user management features as what Mokka provides is not considered to be change.

Compared versions:
* WireMock version: 2.26.0<br>
* Mokka version: 0.5.0

| Feature | Mokka | WireMock |
| ------- | ----  | -------- |
| Stubs Management (CRUD) | + | + |
| Stubs Management - Disable | + | - |
| SOAP/HTTP Support | + <BR> BASIC: No matching by request headers/cookies, no multipart support | + |
| REST Support | + <br> BASIC: No matching by request headers/cookies, no multipart support| + |
| Create stubs from OpenAPI spec | - | - |
| JMS Support | + <br> Embedded ActiveMQ | - |
| Proxying | -  | +  |
| Record and Playback | -  | +  |
| Simulating Faults | - | + |
| Response templating | + <BR> Using Groovy | + <BR> Using Handlebars |
| Stubs stored in | Database | JSON files |
| Stubs modifications history | + | - |
| Interactions log | + <br> Stored in database | + <br> Stored in memory |
| File serving | + | + |
| Fake Payment Gateway | + <BR> BlueMedia | - |
| Admin API | - | + <BR>JSON API, Java API |

So the WireMock already covers most of the requirements. The main differences:
* "Stubs Management - Disable" - use Stub Mapping Metada to define "active" property? __TODO__
* "Create stubs from OpenAPI spec" - have to implemented in Mokka and WireMock anyway. __TODO__
* "JMS Support" - to be verified __TODO__
* "Response templating" - using "Handlebars" are not necessarily a drawback. It seems to be far more elegant and easy to use than Groovy. Also safer from security point of view. __TODO__
* "Stubs stored in" - we can try to provide database-based custom implementation of `MappingsSource`
* "Stubs modifications history" - __TODO__??
* "Interactions log" - Saving to database may be achieved by providing custom implementation of `RequestJournal`. __TODO__??
* "Fake Payment Gateway" - Mokka implementation can be reused


The following solutions were considered:
* continue with Mokka stubs engine
  * \+ flexibility and open architectural decisions in future
  * \- large codebase to maintain
  * \- requires high contribution to develop all missing features
* adopt WireMock sources and maintain them to fulfill all the requirements
  * \+ large set of production-ready features provided at start
  * \+ flexibility and open architectural decisions in future
  * \- large codebase to maintain
  * \- no easy way to upgrade WireMock
  * \- no support of WireMock community
* adopt WireMock as library and use all possible extension points
  * \+ WireMock core implementation remains untouched, new feature are provided using well designed extensions points
  * \+ small codebase to maintain
  * \+ WireMock bugs are handled by the community
  * \+ upgrading WireMock should be straightforward (as long as no breaking changes are introduced to WireMock APIs)
  * \- some future architectural decisions or feature considerations may be limited by WireMock architecture
  * \- in unknown feature WireMock license may change or community support may drop
  * \- we fully rely on WireMock development lifecycle

## Decision

Adopt WireMock as library and use all possible extension points.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
