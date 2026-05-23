# 7. No spec mediatypes in AMF operations

Date: 2021-07-29

## Status

Accepted

## Context

On AMF 5 Beta's first iteration "domain+syntax" mediatypes like "application/swagger20+yaml" were
used to decide how the syntax and the domain were to be parsed. This was especially useful to
validate, transform and render units using compound configurationts (API, WebAPI, RAML, OAS)

This is controversial as:
- Resulting mediatypes are strange to the end-user and are not standard. Besides we could
only handle a specific ordering in domain and syntax. A mediatype formed by syntax+domain
couldn't be parsed.
- Clients that used a specific configuration like RAML10 or OAS30 had to specify the mediatype
although the configuration they used already specified their intended domain and syntax.

## Decision

Remove those compound mediatypes and instead only keep them for syntax purposes when needed.

## Consequences

- Only parsing will remain generic. The client will have to use specific configurations
to validate, transform and render.
- All configurations can render to JSONLD by using the "application/ld+json" mediaType
- The unit's spec will have to be returned in the parsing result so that the client
can select an appropiate configuration.
- Composite configurations can't be used to validate model or transform. They can only render
to JSONLD
