# Use of a logging framework

*   Status: accepted
*   Proposers: trestini
*   Deciders: trestini
*   Date: 2018-05-05

## Context and Problem Statement

Use of a logging mechanism other than javascript's console.log should provide more feature in logging.

## Decision Drivers

*   `console.log` is default for aws lambda and is simple, however have no features other then plot a text to be viewed somewhere
*   Startup time and memory consumption are very important factors
*   Complete log solutions like `winston` provide a [lot of features](https://github.com/winstonjs/winston)

## Considered Options

*   Simple `console.log` calls
*   Wrapped `console.log` calls
*   `winston` logging framework

## Decision Outcome

Chosen option as for "wrapped `console.log` calls". Since `console.log` is just a simple way to log things, it doesn't meant for more advanced logging purposes. `winston` came to fill this gap with a complete logging solution for nodejs applications. However, in the scope of a lambda function, specially in a AWS environment, the major part of those features will not be used (for example the transports, coloring, advanced templating). 

In this sense, wrap a `console.log` with some basic features like leveling, and basic templating can fit better to current context. Only for the sake of *futurism*, the wrapper must be implemented following the same interface of `winston` (eg: `logger.info(...)`, `logger.error(...)`, etc).

## Pros and Cons of the Options

### Simple `console.log` calls

*   Good, zero-coding, already implemented
*   Bad, lack of features like leveling and pattern

### Wrapped `console.log` calls

*   Good, based on `console.log`
*   Good, needed features could be implemented on demand
*   Bad, effort of implementation something that is not the core business of the application

### winston framework

*   Good, *de-facto* default for node.js logging
*   Good, lots of features
*   Bad, lots of features :-) which for a lambda context could bring unecessarly overhead
