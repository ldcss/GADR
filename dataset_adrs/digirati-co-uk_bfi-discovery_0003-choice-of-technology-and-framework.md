# Choice of Technology and Framework

* Status: proposed
* Deciders: Daniel Grant <daniel.grant@digirati.com>, Gary Tierney
  <gary.tierney@digirati.com>, Stephen Fraser
  <stephen.fraser@digirati.com>
* Date: 2021-02-16

## Context and Problem Statement

To deliver BFI's IIIF Universal Viewer auditing platform, custom
deliverables must be produced to support the serving of the Universal
Viewer, and an underlying API which records audit events and persists
them into a database.

This ADR provides options on technologies and frameworks which can be
used to produce these deliverables.

## Decision Drivers

* Ability for Digirati to rapidly deliver the solution.
* Long-term support and stability of the technology and framework
  choices.
* Ease of deployment across different environments / operating systems.
* Robustness and performance of the solution.
* Any technology and framework should be open source.

## Considered Options

* Kotlin (https://kotlinlang.org/) with Spring (https://spring.io/)
* TypeScript (https://www.typescriptlang.org/) with Express.js
  (https://expressjs.com/)
* Python (https://www.python.org/) with Django
  (https://www.djangoproject.com/)

## Decision Outcome

Kotlin is selected as the solution owing to Digirati's vast experience
with the JVM, and when combined with Spring will make this the
deliverables straightforward.

Kotlin does not have the boilerplate cost associated with Java, and as a
result internal there should be fewer barriers in identifying and
understanding the domain specific code required for the deliverables.

In addition, since Spring handles significant amounts of the heavy
lifting, we do not expect to consume time writing code that is not
concerned entirely with handling these audit events.

### Positive Consequences

* Faster development cycle for the parts of the auditing platform which
  require custom code.
* Spring can provide both the Universal Viewer assets and the API,
  unifying everything under one service and keeping authentication
  simple
* The deployment is straightforward, whether using a containerisation or
  deploying directly onto a bare metal server.

### Negative Consequences

* Lack of JVM / Kotlin experience within internal BFI teams.

## Pros and Cons of the Options

### Kotlin with Spring

Spring is a well known framework for building applications on JVM
platforms. It has been the industry leader in the Java space for a long
time and as a result is capable of solving the majority of technical
requirements we'd encounter during the delivery of the solution.

Kotlin is a relatively new technology when compared to Java, however it
compiles to bytecode and thus runs on a JVM. As a result it offers
interoperability both ways between Java and Kotlin code. Kotlin's core
strength is the ability to write code unconstrained by the boilerplate
of Java while still having the entire Java ecosystem available as
tooling.

#### Pros

* 20+ years of combined experience with JVM and Spring applications.
* Tooling for the JVM and Kotlin makes developing the solution a
  plug-and-play experience.
* Spring Boot framework suits itself well to rapid development.
* Zero-configuration OAuth 2.0 / OIDC integration available from Spring.
* JVM as a deployment target may make bare-metal deployment easier when
  running existing JVM applications.
* Rich documentation and examples are available.

#### Cons

* Limited / no experience at BFI with writing code for the JVM.

### TypeScript with Express.js

Express.js is a barebones web server implementation for the NodeJS
platform. The web server itself is mostly a skeleton, which is usually
extended using middleware that is able to intercept requests and
responses, reading and writing to them as needed to add additional
functionality. There is a lot of existing middleware for Express.js
developed by the community that could be used to meet the solution
requirements (e.g. session management, OAuth 2.0 / OIDC integration,
etc).

TypeScript is a loosely typed programming language that sits over the
top of JavaScript and adds strict validation over program source code,
similar to a Java codebase. This allows the writing of code that stays
clear and maintainable over time, by using the type system to document
itself. A fully TypeScript codebase requires that dependencies also have
TypeScript bindings available.

#### Pros

* Digirati have experience building lightweight Express.js applications.
* Rapdi development can be achieved through constant recompilation
  (e.g., watch style commands).

#### Cons

* Less of an "out of the box" solution.
* Poor documentation, outdated examples, frequently changing ecosystem.

### Python with Django

Django is a web framework intended for rapid development in Python.
Similar to Spring, it comes with the majority of the tools that are
needed in building a modern web application out of the box which allows
developers to get started writing domain specific code.

#### Pros

* Internal BFI staff have experience with Python.
* Django is built for rapid development through constant recompilation
  (e.g., watch style commands).
* Rich documentation, lots of examples, stable versioning.

#### Cons

* Digirati have more experience in delivering identity and access
  management with JVM languages.
