# 4. Use ElasticSearch for search

Date: 2017-05-25

## Status

Accepted

## Context

Following user research a more comprehensive text search engine was needed in order to be able to
use more complex searches (and/or), full phrase search, stemming as well as geolocation searches.

## Decision

A review of ElasticSearch and Funnelback was undertaken [here](https://docs.google.com/document/d/10xK0on4gzrB1ImZHk3Z_PoCr7V_aUpiieuLdQDg4OwQ/edit)
and [ElasticSearch](https://www.elastic.co/products/elasticsearch) was chosen as a candidate due to the fact that it was 
open source and had comprehensive documentation with an established community around it.
(Funnelback)[https://www.funnelback.com/] was discounted due to it being closed-source and for 
it's lack of community support.
A  Docker image of GP data ([profiles-db-elastic](https://hub.docker.com/r/nhsuk/profiles-db-elastic/))
running an ElasticSearch instance has been created for use by this application and possibly by other applications.

## Consequences

We found that by swapping the technology solution for search, will enable us to add the new functionality the users need
and focus on the domain problems rather than solving search-related issues.
