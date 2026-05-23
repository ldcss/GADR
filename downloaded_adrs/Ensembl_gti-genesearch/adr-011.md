# ADR 011: Multiple location support

## TL;DR
Location and numeric support needs overhauling to support several use cases.

## Context
An important use-case is to search for genes found in multiple regions of the genome e.g 1:1000-1500,1:3000-3600,5:2000-3330 etc. This needs to be supported for searching genes and variants.

e.g.
```
http://localhost:8080/api/genes/query?query={"genome":"homo_sapiens","location":{"seq_region_name":"1","start":"45000","end":"96000"}}
http://localhost:8080/api/genes/query?query={"genome":"homo_sapiens","location":[{"seq_region_name":"1","start":"45000","end":"96000"},{"seq_region_name":"1","start":"107000","end":"196000"}]}
```

Currently, location is dealt with using `QueryType.RANGE` that `DefaultQueryHandler` processes a single location string to start, end etc. but this approach will not work with multiple values. It is also likely that different search engines need to search in different ways.

In addition, there is a separate need for general range and numeric queries.

## Decision
We will do the following:
* `LOCATION` will become a new `QueryType` which will be handled separately by each search implementation and accept one or more strings of the format `seq_region:start-end:[strand]`
* `DefaultQueryHandler` will no longer deal with locations.
* `QueryType.RANGE` will be removed
* `QueryType.NUMBER` will be added and processed by each search implementation, supporting numbers of the form `([<>]=)?[0-9.-]+(-[-0-9.]+)?`

## Status
Under development

## Consequences
Original examples will not work though `{"seq_region_name":1, "start":>45000, "end":<96000}` should work fine.

## Tags
