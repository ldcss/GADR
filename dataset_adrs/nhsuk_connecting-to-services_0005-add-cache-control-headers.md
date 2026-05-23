# 5. Add cache control headers

Date: 2017-08-17

## Status

Superseded ([0007](https://github.com/nhsuk/connecting-to-services/blob/master/doc/adr/0007-remove-cache-control-headers.md))

## Context

Cache control headers can be used to prevent a client's browser from
re-requesting a page that has not changed, and may be leveraged by proxies to
return the same cached pages for multiple clients.

## Decision

Cache-control headers will be added to all valid requests. 500 and 404 errors
will not be cached.

## Consequences

Clients will use a locally cached version of a page where possible, reducing
server load.
