# Server Side Caching

**User Story:** [EASI-1505](https://jiraent.cms.gov/browse/EASI-1505)

There are certain types of calls that EASi makes that are considered "expensive". This usually takes the form of something like a 3rd party API call (CEDAR Core, for example), or a database call.

Caching is often a good way to effectively reduce the number of times the expensive calls are made, at the cost of having data be less up to date.

## Considered Alternatives

* In application memory caching
* Caching with a database
* Caching with Redis

## Decision Outcome

* Chosen Alternative: In application memory caching for now, Redis caching later.

Right now we likely don't have the engineering staff to implement all the infrastructure that a Redis instance would require. Since implementing an in-memory cache is a relatively simple task (especially compared to the massive benefit that we get from it), it seems worthwhile to implement it for now, and come back and replace it with Redis at a later time.

Additionally, the main con of in-application memory caching (that it's not shared across multiple tasks) is not a huge deal at this time, since we typically are only running 1 task at a time due to our workload being relatively low.

## Open Questions

- Is there a way to avoid (or minimize) the amount of times that a user "feels" the load time of an expensive call?
  - A few potential options:
    - Periodically "seed" the cache, rather than populating it when a request is made for the data
      - This has the upside of always having users hit the cache directly, but the downside is that we'd have to write some scheduled code to periodically seed the cache (Lambda?)
    - Have the cache never expire, and always return data from the cache, but instead of refreshing the cache _before_ returning data to the front-end, refresh the cache _after_ we return data
      - This has the upside of also always returning from cache (fast!), but the (major) downside of potentially having data from the cache be _very_ old.

## Pros and Cons of the Alternatives

### In application memory caching

* `+` Very easy to implement. (See [the POC branch](https://github.com/cms-enterprise/easi-app/compare/EASI-1505/go-cache-poc) for an example of how to implement it.)
* `+` Requires no changes to infrastructure
* `+` Likely has the lowest response time out of all the available options
* `+` Can easily be temporarily introduced and later replaced with another solution
* `-` Cache is not shared across multiple servers (exists per ECS task)

### Caching with a database

* `+` Requires no changes to infrastructure
* `+` Is persistent across multiple servers
* `-` Caching logic would have to be manually written (columns to track timestamp, cleaning the DB of old data, etc.)
* `-` Is going to be the slowest option in terms of response time
* `-` Doesn't solve caching DB queries at all

### Caching with Redis

* `+` Very fast response time (sub-millisecond)
* `+` Solves caching in a lot of different contexts (API queries, DB queries, etc.)
* `+` Redis is purpose-built to solve caching. Supports lots of different options out of the box
* `-` Requires introducing new infrastructure
