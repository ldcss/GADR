# 1. Using GraphQL for the API Layer

Date: 2021-08-09

## Status

Accepted

## Context

During the E&I phases of work for the Administrative Office of the Courts we are exploring the use of an API as a centralized source of truth for court data both as a means to access the data as well as manipulate it. One of primary challenges faced by the AO is the diverse ways different courts access and use data in their day-to-day work. Different courts have different conventions and rules for processing cases and it has been difficult to design a single software solution for managing their cases. 18F's Path Analysis recommended using an API as a central tool that can offer flexible access to data, while still allowing courts autonomy over how this data is used.

The convention of the REST APIs is battle-tested and well-understood. REST APIs define resources as HTTP endpoints and associates them with HTTP verbs such as GET, POST, PUT to define actions. However, REST APIs present some difficulties:

- They are difficult to change once clients start using them, leading to simultaneously maintaining various versions of the API
- It is usually not feasible to dynamically define what data is returned from the API, leaving clients with either more data than they need because that's what the endpoint returns, or requiring them to make multiple requests for related data.

GraphQL is a different API paradigm designed specifically to address issues of efficiency and flexibility.

## Decision

For this phase of work the primary API interface will be GraphQL, although the domain logic of the application should be independent enough to allow this to change in the future.

## Consequences

GraphQL moves many of the difficulties of processing data from the frontend to the backend. With a traditional REST API, the front-end code often accepts whatever form of data the API sends and then is left to manipulate, merge, and filter this data to suit the needs of the user. With GraphQL the front-end can define with some precision exactly what data it needs and what shape that data should take. Also, because a schema is central to GraphQL, front-end developers can discover specifically what type of data is available making data validation easier. For the front-end developer accustomed to REST, a GraphQL API will require some additional learning.

The work of serving a GraphQL API however, is more difficult on the backend. Rather than defining specific endpoints that send specific data, the GraphQL server needs to parse JSON queries that take a variety forms and can mix and match data potentially from many sources. This presents some n+1 efficiency problems when a single request from a user leads to many requests to a database. This issue is manageable with tools such as DataLoader layer and through smart caching of results within a single query. We have not, however, explored using this yet since our API is currently simple enough to not need them.
