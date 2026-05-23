# 2. Start with modular monolith backend

Date: 2021-01-07

## Status

Accepted

## Context

Whether to start with a Microservices or not. There are 2 schools each advocating for the exact opposites.

### 1. [Don’t start with a monolith](https://martinfowler.com/articles/dont-start-monolith.html) - Stefan Tilkov 

> Microservices’ main benefit, in my view, is enabling parallel development by establishing a hard-to-cross boundary between different parts of your system. By doing this, you make it hard – or at least harder – to do the wrong thing: Namely, connecting parts that shouldn’t be connected, and coupling those that need to be connected too tightly. In theory, you don’t need microservices for this if you simply have the discipline to follow clear rules and establish clear boundaries within your monolithic application; in practice, I’ve found this to be the case only very rarely


### 2. [MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html) - Martin Fowler 

> The first reason for this is classic Yagni. When you begin a new application, how sure are you that it will be useful to your users? It may be hard to scale a poorly designed but successful software system, but that's still a better place to be than its inverse. As we're now recognizing, often the best way to find out if a software idea is useful is to build a simplistic version of it and see how well it works out. During this first phase you need to prioritize speed (and thus cycle time for feedback), so the premium of microservices is a drag you should do without.

> The second issue with starting with microservices is that they only work well if you come up with good, stable boundaries between the services - which is essentially the task of drawing up the right set of BoundedContexts. Any refactoring of functionality between services is much harder than it is in a monolith. But even experienced architects working in familiar domains have great difficulty getting boundaries right at the beginning. By building a monolith first, you can figure out what the right boundaries are, before a microservices design brushes a layer of treacle over them


## Decision

We believe that in the early stages, when domain is still being explored and the project is small, monolith is the 
easiest and safest way to start. 

We also acknowledge that as the project complexity and demand for shorter time-to-market increases, microservices 
architecture becomes more and more valuable.

Therefore, we decide to start with the monolith, with the strict boundaries between the modules, in order to benefit from 
the ease of initial development and enable ourselves to evolve towards the microservices in the future  

## Consequences

- We will have to worry less in the beginning about the packaging, deployment, distributed tracing, circuit breaking and other prerequisites that
microservices come with
- We will focus more on the domain exploration and overall user experience
- Special care to be taken for the code organization to achieve high cohesion and loose coupling
- Codebase will be locked down to the same programming language and (to some degree) technologies
