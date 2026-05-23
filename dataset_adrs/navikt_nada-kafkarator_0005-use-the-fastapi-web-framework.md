# 5. Use the FastAPI web framework

Date: 2020-02-28

## Status

Accepted

## Context

Our application needs to supply some web endpoints for healthchecks, so we need to select a web framework.
There are a multitude to choose from, but we have some preferences:
- We want something that is well maintained and has a community
- We want something that has decent performance
- As a learning experience, we want to use one of the many async frameworks

The front contenders seems to be Sanic, FastAPI, Tornado, Vibora and Quart.

Tornado seems to be somewhat dated, as it was created before Python had async built in.
Vibora is a relatively new project, with uncertain community adoption.
Quart is API compatible with Flask, which is the most common non-async web framework.
Sanic seems to be the most popular of the async frameworks.
FastAPI is by far the most performant of them all.

## Decision

We will use FastAPI, because of the performance, and some of the interesting features.

## Consequences

Since our application is going to be relatively simple, it should be possible to switch frameworks with relative ease. That allows us to experiment to find the framework we prefer. 

FastAPI gives us API documentation automatically, if we write our code in the right way, which is a nice bonus.
