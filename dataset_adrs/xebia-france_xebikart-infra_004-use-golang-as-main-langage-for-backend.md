# Use Go as main programming language for backend

* Status: Accepted
- Date: 2019-03-11
- Deciders:
    - achotard
    - jpthiery

## Context and Problem Statement

We want to code a backend that will handle inbound informations through the
message broker, and expose them to the dashboard front-end.

What programming language should we use?

## Decision Drivers

- Should be interesting (fun, new, ...) for people
- Either already adopted by Xebians or not too hard to adopt based on existing
  knowledge
- Library support for our usecases

## Considered Options

- Go
- Elixir
- Scala
- Kotlin
- Java
- Other languages

## Decision Outcome

Chosen option: **"Go"**, because:

- It has good library support for things such as **HTTP/2** and **Protobuf**
  (separately, we're not talking about gRPC  here). This will help establish
  strong bidirectionnal and persistant streaming with the dashboard (HTTP/2).
  It will also open the way to Protobuf serialized messages over the message
  bus that will maybe comme in addition to RabbitMQ.
- People on the project want to play more with it!
- It seems appropriate for small (micro)services like the one we're going to
  build

However, we are **not excluding other languages** depending on usecases and
wishes of people working on it. We want people to contribute so we won't force
anyone to use a given language. **People are free to use the language they
want**, but we'll try to have **Go as a default main language as much as
possible**.
