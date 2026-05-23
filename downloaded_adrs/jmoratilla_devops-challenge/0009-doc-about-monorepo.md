# 9. doc-about-monorepo

Date: 2020-02-25

## Status

Accepted

## Context

Microservices are complex because they are small and can use different languages
 and different stacks to run: java, spring, jakarta, python, flask, tornado, ruby
 rails, sinatra, mysql, postgresql, mongodb, redis...

There are so heterogeneous that sometimes we need to set a common way to work with
 them.  Each microservice has a different life-cycle, some are update more 
 frequently, others are not.

Usually, when apps differs in their life-cycle speed, incompatibilities will come
 up.  Those incompatibilities can make the system get down.  And keeping an 
 updated and acurated matrix of compatibilities is a pain.

A way to minimize this risks is to put all code in the same repository, but not as
 a monolithic application, but in separate folders.  This has some advantages 
 like:

- all code is tested at the same time
- transversal refactors can be easy
- compatibility matrices are simplified


## Decision

To use a monorepo to keep all code together and deploy it at the same time.


## Consequences

The main advantage is that all code is in the same repository.  This reduces
 the complexity of the system.

Also, all the versions are updated at the same time, no matter if the app
 has changed in this release or not.  It just will be released with no changes
 but keeped at the same level than the other apps included in the monorepo.

Some disadvantages are:

- the size of the repo, as it will grow more quickly
- it will slow some automated task, like building or testing
- more users working on the same repository implies more branches and more
  activity in the same history, doing more difficult to read.
