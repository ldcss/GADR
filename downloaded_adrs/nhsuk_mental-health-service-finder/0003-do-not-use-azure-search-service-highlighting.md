# 3. Do not use Azure Search Service highlighting

Date: 2018-08-16

## Status

Accepted

## Context

[Azure Search Service](https://docs.microsoft.com/en-us/rest/api/searchservice/)
has the ability to return results with the search term hits
[highlighted](https://docs.microsoft.com/en-us/rest/api/searchservice/search-documents#highlightpretagstring-optional).
The searches submitted by the application add a wildcard character (`*`) to
each term. The reason for this is to have results returned where the term
matches the beginning of the word e.g. `prac` with return results with the word
`practice` in (and any other word starting with `prac`). A consequence of this
is the highlighting returns full word matches e.g. searches for `prac` will
return highlights as `<span class"highlight">practice</span>` whereas only the
exact term entered should be highlighted. There is no option within the search
service to have only the exact term entered highlighted.

## Decision

Given the search service is not able to fulfil the requirement of exact term
highlighting the decision is to highlight the results by the application
server, once the results have been returned from the search service.

## Consequences

The consequences are:
* (A relatively small amount of) Additional code is required within the
  application
* The request to and the response from the search service is smaller and less
  involved
