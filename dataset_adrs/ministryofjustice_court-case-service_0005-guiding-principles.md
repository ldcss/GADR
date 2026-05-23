# 5. Guiding principles for `court-case-service` API design

Date: 2021-07-16

## Status

Under review

## Context

The implementation of [PIC-1135](https://dsdmoj.atlassian.net/browse/PIC-1135?focusedCommentId=163988) raised questions about what is the appropriate approach for serving new data to the prepare-a-case app, and in particular stressed the need for error handling by `prepare-a-case` where graceful degradation from partial failures is needed. The question was raised as to whether `court-case-service` should be coupled closely with `prepare-a-case` and is notionally a dedicated gateway for it or whether it should be treated as a general purpose API which may be consumed by multiple consumers.

## Decision

1. All data stored by `court-case-service` is considered its own domain and should be treated as a general purpose api
2. All endpoints composing data on behalf of `prepare-a-case` are not intended for consumption by other clients and should provide all data needed on a given `prepare-a-case` page as efficiently as possible
3. The exception to point 2 is the case where errors in the retrieval of certain pieces of data are expected and need to be isolated. In this case data to be isolated should be served as a separate endpoint which will fail fast. `prepare-a-case` can then handle it simply as a failed HTTP call. See [PIC-1135](https://dsdmoj.atlassian.net/browse/PIC-1135?focusedCommentId=163988) for an example of this.


## Consequences

In practice this means that points 2 and 3 apply to everything under `/offenders`. To cement this distinction we should aim over time to separate out these two APIs in the documentation by applying Swagger tags of 'General purpose' or 'prepare-a-case'.

As it stands there are known exceptions to principle 2 where multiple API calls are made on a given page on `prepare-a-case` (e.g. at the time of writing convictions and sentences) which we should also aim to resolve where possible.

Principle 2 is based on the assumption that no other consumer is going to need the same composition of data as `prepare-a-case`. As such `court-case-service` should not own any business logic outside of its core domain (cases), and only provides a view of other services' data. If this is not the case then the above principles should be re-evaluated.
