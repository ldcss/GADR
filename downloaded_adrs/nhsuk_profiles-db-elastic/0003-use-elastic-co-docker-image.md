# 3. Use Docker Image from elastic.co

Date: 2017-06-15

## Status

Accepted

## Context

[ElasticSearch](https://www.elastic.co/products/elasticsearch) is a Java based search engine built on top of technologies like Lucene and Solr. It is open source software which can be freely [downloaded](https://github.com/elastic/elasticsearch) and installed on a number of operating systems. It is also freely available from elastic.co as a Docker image and as a subscription based SaaS offering. The SaaS option is discounted in ADR [0002](0002-use-docker-image-for-elastic.md).

## Decision

We will use the official Docker image provided by elastic.co.

## Consequences

- There have been concerns raised in the ES community as a result of the Docker images being hosted at [elastic.co](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html) rather than Docker Hub (see the comments [here](https://hub.docker.com/_/elasticsearch/)) specifically to do with historic image versions. It seems from the ES response [here](https://discuss.elastic.co/t/consider-hosting-docker-images-on-docker-hub/85214) and manual inspection that recent versions are all available so this is not likely to be a problem for us.

- X-Pack: the Docker image includes X-Pack security module (free subscription level) which does not allow the default username and passwords to be changed without paying a subscription. The inability to change default user name or password presents a risk. This will need addressing before the service is presented to users by default. This could be by paying the X-Pack subscription, building our own ES image with a free security alternative (e.g. [SearchGuard](https://sematext.com/blog/2017/05/22/elasticsearch-kibana-security-search-guard/)) or by using the ES SaaS [offering](https://www.elastic.co/cloud/as-a-service).  
