# 2. API versioning strategy

Date: 2020-01-20

## Status

Accepted

## Context

Regardless of how well planned an API is, it's a sure bet that business requirements WILL eventually dictate that backwards-incompatible changes will be made to the API. Versioning the API is a necessity.

The OPG-Data API must implement versioning. Must be RESTful, and offer as much flexibility with regard to future hosting/infrastructure as possible.

Sadly there is no real consesus on the best approach to versioning an API, with several of the 'big players' opting for different strategies. There are pros and cons to each approach.

An exploration of various API versioning strategies may be found here [versioning-strategy.md](../supporting-notes/versioning-strategy.md)

## Decision(s)

* We will be using semantic versioning [https://semver.org](https://semver.org) see [versioning-strategy.md#semver](../supporting-notes/versioning-strategy.md#semver) for more
* We will implement versioning via the Content Negotiation using the Accept header, as per [versioning-strategy.md#options-5](../supporting-notes/versioning-strategy.md#options-5). This seems the most future proof, most RESTful solution.

This necessitates our own vendor content type. Examples:

* `application/vnd.opg-data.v1+json` (v1 presented as JSON)
* `application/vnd.opg-data.v1+yml` (v1 presented as YAML)
* `application/vnd.opg-data.v1` (v1 presented as JSON)
* `application/vnd.opg-data` (latest version, presented as JSON)
* `application/json` (latest version, as JSON)

The final two are dangerous in that the version presented will change over time without warning.

See also: [4. Content Negotiation](0004-content-negotiation.md)

* At any given time, the API will allow requests from two major versions: The latest version and the previous, deprecated version.
* All API responses will contain a x-current-api-version which will be set to the current version of the API in addition to an x-api-warn header when calling any deprecated API endpoints.
* A Versions Timeline Document kept up to date with all changes and presented at an endpoint `api/release-info` from within the API itself
* When using a version-non-specific content-type as with the final two examples of the preceding list, an x-api-warn header will be returned, warning the client to specify a version

## Consequences

* Simple for API consumers to request version and representation
* HATEOAS-friendly
* Cache-friendly
* RESTfully Keeps a URI for a resource the same
* It opens up the possibility of adding resource-specific versioning in the future, eg `application/vnd.opg-data.donor.v1+json` would be a JSON representation of a donor resource at version 1
* API developers must be made aware about how the Accept header is being used
* Browsers may have trouble understanding nonstandard content-types. However, browsers are almost certainly not the target consumer of the services.

## Note

As detailed in [OPG-Data API Specification](0003-opg-data-api-specification.md), our API specification borrows heavily from the [JSON-API](http://jsonapi.org/format/). Where our documentation does not specify otherwise, it should be assumed that the JSON:API standard applies.