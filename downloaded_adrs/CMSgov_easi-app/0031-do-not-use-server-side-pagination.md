# Do Not Use Server-Side Pagination

**User Story:** [EASI-1447](https://jiraent.cms.gov/browse/EASI-1447)

In cases where the volume of data being shown on a page is large, server-side pagination (SSP) can range from being useful in reducing initial page load times, to being mandatory for prevention of page crashes when running out of memory. As long as we're using pagination or virtual scrolling on the client-side, we are unlikely to ever run into the later issue, based on our current understanding of EASi's use-cases.

## Considered Alternatives

* Do not implement SSP
* Implement SSP using an offset-based strategy with GraphQL
* Implement SSP using a cursor-based strategy with GraphQL

## Decision Outcome

* Do not use SSP for now, consider a cursor-based strategy in the future if data volumes grow large enough to cause long initial load times

Currently, the largest volume of data that EASi loads in any one view is CEDAR system list data. With in-memory caching of this data, initial load times are in the range of 700 to 800 milliseconds. After that load, the data remains available for client-side pagination without any subsequent loads from the server. As a result, the user experience is seamless when doing other things like sorting, filtering, and browsing through the paginated data.

## Open Questions

- What is the limit to what we would consider an acceptable initial load time for a view?

- How might the data we load in EASi grow over time?

## Pros and Cons of the Alternatives

### Do Not Use SSP

* `+` No significant code changes need to be made
* `+` Reduces complexity of the codebase, especially when implementing features like sorting, filtering
* `+` Smooth user experience once data is initially loaded (no subsequent data loads for paging, sorting, or filtering)
* `-` Longer initial load times for views that load large numbers of records

### Implement SSP using an offset-based strategy with GraphQL

* `+` Limits initial load times
* `+` Prevents page crashes due to running out of memory (not likely to be an issue for EASi)
* `+` Simplest SSP strategy to implement
* `-` Increases complexity of the codebase, especially when implementing features like sorting, filtering
* `-` Causes a less smooth user experience when navigating the data, filtering, or sorting because data must be loaded from the server each time

### Implement SSP using a cursor-based strategy with GraphQL

* `+` Limits initial load times
* `+` Prevents page crashes due to running out of memory (not likely to be an issue for EASi)
* `+` The most flexible SSP strategy, allows a cursor-based SSP strategy, and also allows offset-based and ID-based SSP strategies by setting the cursor equal to an offset or a record ID
* `-` Increases complexity of the codebase, especially when implementing features like sorting, filtering
* `-` Causes a less smooth user experience when navigating the data, filtering, or sorting because data must be loaded from the server each time
