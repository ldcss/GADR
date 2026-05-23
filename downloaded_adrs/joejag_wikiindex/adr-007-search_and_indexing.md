# Search choices

**DEPRECATED BY ADR-008**

## Context

* As per ADR-001
* In memory search is unacceptably slow

## Decision

* We will use Clucy which is a Clojure library on top of Lucene

## Consequences

* Clucy takes over an hour to index. This is probably acceptable for a file that only updates twice a month
* Given this startup time, it is undesirable to run in memory
* The response time is now 28ms
* We should move to ElasticSearch as moving the loading of the index to a separate process would require the same amount of work
