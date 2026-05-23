# Search choices

**DEPRECATED BY ADR-007**

## Context

* We need to index and search a 32Mb XML file.
* The search is across multiple fields.
* Only one search word is used.
* We currently don't have any external platform tools like Mongo, ElasticSearch, an RDMS
* We do not know how often the XML file will be updated.

## Decision

* We will parse the file on startup, store it as a clojure collection that is available throughout the system.
* We will do this before the web server http port is available.
* Searches will be performed against this in memory collection.
* The app would need to be restarted to parse a new XML file, unless an additional endpoint is added.

## Alternatives considered

### Elastic Search

* We could use ElasticSearch.
* A separate process would convert the XML to JSON then index it into ElasticSearch.
* Our web app would then pass on the search request from the user to ElasticSearch.

### A Document Database

* A document database like Mongo could store a JSON representation.
* It's native search would probably .
* This approach can be taken it the atom approach takes too long to index the XML file on startup.

### Lucene in-process

* Use the Clucy library to create an in memory Lucene index

## Consequences

* The application needs 0.5Gb RAM to run with 130K documents loaded in memory, 400mb seems to be due to our approach
* Search is O(n)
* The average response time with 10 concurrent requests is 2 seconds, which will probably be unacceptable
