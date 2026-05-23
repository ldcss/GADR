# 1. Use GraphQL for API
Date: 6/18/2018

## Status
Accepted

## Context
Because this project is going to be delivered as a Beta project by the end of the year, it will be likely that its needs will grow as feedback from real users begins to filter in, as new ideas are conceived, new platforms are required, and as sources of funding are renewed. In order to accommodate these concerns, CHIP needs a simple, flexible, yet powerful API that is well situated for both changes in feature requirements and changes in technology. 

## Decision
GraphQL is a specification for an alternative to traditional REST APIs that provides a declarative development experience where you tell your program _what_ you want to happen and the GraphQL library will handle the _how_. It was initially developed by Facebook in 2012, announced by them in 2015, and has since grown exponentially to where 2018 will likely see more new APIs being written in GraphQL than in REST. 

The Absinthe library is a fully-featured, spec-compliant GraphQL implementation for Elixir and Phoenix applications and will be used for this project.

## Consequences
Some of GraphQL's key benefits include:

- Declarative approach is all about writing code that says _what_ rather than _how_
- Rapid iterations on the front-end because you don't have REST endpoints dependent upon your UI/UX
- Prevents over/under fetching: ask for what you need and get what you need, no more no less
- Better analytics and insights into what data is being requested
- Strongly typed schema serves as a contract between front and back end
- Built in validation
- Built in API explorer
- Provides a foundation for more easily expanding the app with new data and to new platforms

Some things developers will need to be aware of:

- It's not a panacea or silver-bullet, if it makes more sense to create a REST or RPC endpoint to handle a particular request, don't try to force it into GraphQL
- Though Facebook has been using it for 6 years, it's still a new technology in the grand scheme of things. Many developers still haven't even heard of it, though I expect that will be changing quickly throughout 2018 an 2019.


