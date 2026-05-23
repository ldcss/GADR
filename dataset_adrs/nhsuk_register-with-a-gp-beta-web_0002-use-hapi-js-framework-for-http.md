# 2. Use hapi.js framework for http

Date: 30/01/2017

## Status

Accepted

## Context

As we start to standardise on what our services look like we want to use the
best tools for the job when it comes to node web frameworks. Hapi is more of a
framework than [express] and is more modular allowing many developers to work on
a single project without trampling over each others' routes.

## Decision

We have decided to use [hapi] as our http server. 
There are many other [alternatives] but none are as actively developed as Hapi

## Consequences

There is less documentation for [hapi] vs [express] because it isn't as popular
however the documentation that exists is good and up to date.

[hapi]: https://hapijs.com/
[express]: http://expressjs.com/
[alternatives]: http://expressjs.com/en/resources/frameworks.html
