# 14. better-data-transformations

Date: 2019-12-14

## Status

2019-12-14 proposed

## Context

Creating new and updating existing data transformations, whether from APIs or the database, is still a pain point. After many refactors I feel that the abstractions I am using are not helping. The goal for the data transformations were:

- Take data from an API or database
- Modify or enrich it
- Save or display the results to the user

To achieve this, there are two abstractions that I rely on:

- Hapi plugins: an interface defined by Hapi server that can add features to the server object.
- Plugin helpers: ad hoc functions that I use to decompose plugin actions.

The problem with these are:

- Mixing of concerns: data transformation and server processes need different abstractions because they should be able to change independently. As it is, I have coupled them together.
- Broken interfaces: related to the first point, [Hapi plugins][hapi-plugins] have an interface that makes them useful for the server. Trying to use the same for creating a data pipeline is very "hacky" - open to frequent changes and bugs.
- There is a better way: data transformations will benefit from a different abstraction solving the current problem and opening up new possibilities.

Two abstractions present themselves:

- Transducers
- Streams

They both create programming interfaces that allow chaining of operations on a data set: e.g. `A |> B |> C` where the input for the next step is the output of the previous.

Transducers are an abstraction implemented by 3rd party libraries while streams are native to [NodeJs][nodejs-streams]. In practice, I would use a library for either approach to deal with [possible pain points][nodejs-streams-readable-streams].

## Decision

In the context of lacking a well established method to build data pipelines in JavaScript, and facing the concern of fragile data transformations then use Streams. They can be used for large files since they have a low memory footprint and can have other uses e.g. request/response streams.

## Consequences

- Learn Streams and adopt an appropriate library.
- Refactor data transformations to use Streams.

[hapi-plugins]: https://github.com/hapijs/hapi/blob/master/API.md#server.plugins
[nodejs-streams]: https://nodejs.dev/nodejs-streams
[nodejs-streams]: https://github.com/substack/stream-handbook#consuming-a-readable-stream
