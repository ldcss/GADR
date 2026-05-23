# 3. Use MongoDB for search

Date: 2017-02-27

## Status

Superseded ([0004](https://github.com/nhsuk/gp-finder/blob/master/doc/adr/0004-use-elasticsearch-for-search.md))

## Context

In order to perform a search on GP or surgery name, a repository of GP Surgeries is needed.
A Docker image of GP data
([profiles-db](https://hub.docker.com/r/nhsuk/profiles-db/)) running a MongoDB
instance has been created for use by other applications and we have chosen to adapt it
via indexes to be able to efficiently be used by this application as well.
The (MEAN stack)[https://en.wikipedia.org/wiki/MEAN_(software_bundle)] has quite a lot of backing as a
software bundle within the community and we use everything except Angular from it's solution.

## Decision

We have decided to use the existing Docker image rather than spend effort
acquiring the data again. We added indexes to ensure our functionality requirements were met, 
without putting to many constraints on the image that is being consumed by other applications.

## Consequences

If there are multiple consumers of the Docker image there might be conflicts on
the data contained within the image, both content and format.

The sharing of the image means any work done on improving the creation of the
image including data refresh frequency will be shared amongst all consumers.
MongoDB provides much more functionality than is required by the application
which may be able to be leveraged in the future.

We have started using the image as a basis of our search in order to deliver the features required
by our users, knowing full well that MongoDB is not a search engine. This was accepted at that 
particular point in time.
