# 1. Use square brackets for query string parameters with multiple values

Date: 2017-08-03

## Status

Accepted

## Context

Query string parameters to drive searches into an API often need to pass in multiple values, used in OR with each other.

## Decision

We will use the PHP-style query string parameter format:
```
/search?type[]=blog-article&type[]=collection
```

## Consequences

On PHP backends this will naturally result in an array.

On Python backends there is no particular support for this format, but multiple values can still be read.

When using `curl` on the command line, the `[` and `]` need to be backslashed or the `-g` option needs to be used:
```
curl 'https://api.elifesciences.org/search?for=naledi&type\[\]=collection'
curl -g 'https://api.elifesciences.org/search?for=naledi&type[]=collection'
```
