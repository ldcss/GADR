# 2. Use Docker to provision and run Elastic Search 

Date: 2017-06-15

## Status

Accepted

## Context

[ElasticSearch](https://www.elastic.co/products/elasticsearch) (ES) is a Java based search engine built on top of technologies like Lucene and Solr. It is open source software which can be freely [downloaded](https://github.com/elastic/elasticsearch) and installed on a number of operating systems. It is also available from elastic.co as both a Docker image and as a cloud service.  The SaaS offering from elastic.co has a cost approaching $100/month for a production set up. Our default approach to provisioning is to use containerisation in general, and Docker in particular. There are no compelling reasons not to use Docker containers to provision and deploy Elastic Search.

## Decision

We will use Docker containers to provision and deploy Elastic Search.

## Consequences

- The use of a Docker image means that we have to manage the provision and scaling of ES ourselves.
- Typical Connecting to Services applications (which are Docker based) should be more performant when using the Docker hosted ES in comparison to SaaS.
 - Running ES as a Docker image hosted on our infrastructure should be cheaper than the SaaS option even taking into account the administrative overhead.
