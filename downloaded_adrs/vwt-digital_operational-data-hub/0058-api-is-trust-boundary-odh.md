# 58. API is trust boundary ODH

Date: 2020-09-30

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

Implements [39. Least privilege access](0039-least-privilege-access.md)

Related to [43. API First](0043-api-first.md)

## Context

 The trust boundary is a boundary where program data or execution changes its level of "trust." The term refers to any distinct boundary within which a system trusts all sub-systems (including data). An example of an execution trust boundary would be where an application attains an increased privilege level (such as root). A data trust boundary is a point where data comes from an untrusted source. For example, user input or a network socket.

Trust boundaries aren’t hard to find: We just need to ask questions like “What are the consequences if this code/data became horribly malicious? Is that likely? Can we defend against it? Do we want to defend against it?”

To deal with trust boundaries, we have all the usual techniques and organizing principles: input sanitization, defense in depth, sandboxing, secure authentication, least privilege, etc.

On the ODH platform the first trust boundary when connecting from outside is the API, which is a result of the [API first](0043-api-first.md) principle. The API implements authentication and authorization (is identity aware), performs input validation and sanitization, protects back-end services from the outside world and is executed with only the permissions required, according to the [principle of least privilege](0039-least-privilege-access.md). This makes the API a trust boundary between the outside world and the platform.

Connecting platform components without an intermediate API lacks this additional layer of defense, thus reducing defense in depth. Using an API also decouples the service provided from its implementation, as the client is not using a platform specific implementation, but the API interface instead, which can be ported to another implementation without impact on the client.

## Decision

We will provide all functionality to external systems through an API, using this as a trust boundary on the ODH platform.

## Consequences

### Advantages

* Additional layer of defense, implementing defense in depth.
* Standardization, reducing trusted computing base.
* Decoupling of client using the API from the platform implementation, providing changability and portability.

### Disadvantages

* Implementation of API is additional cost when in some cases the services provided by the platform would be able to provide the required functionality.
* Implementing a performant http API can be hard for some use cases.

## References

* https://en.wikipedia.org/wiki/Trust_boundary, retrieved 30 October 2020
* https://blog.regehr.org/archives/1576, retrieved 30 October 2020
