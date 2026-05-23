# 2. Versioning of the API

Date: 12th June 2020

## Status

Accepted

## Context

Third-party programme suppliers have begun integrating with [the API](https://github.com/ministryofjustice/hmpps-book-secure-move-api) provided by this service. Our in-house
[client application](https://github.com/ministryofjustice/hmpps-book-secure-move-frontend) has been consuming the API for a while and breaking changes were previously made sparingly 
and with constant communcation so strict versioning wasn't required.

Moving forward we need to be more strict with versioning when there are any breaking changes to the API as
we now have more consumers, including those outside of our team.

## Decision

We will attempt an **API Evolution** approach to support backwards compatability.

When that is not possible, we will support **Global URI versioning**. For example moving from version 1 to version 2 with a breaking
change to the `moves` endpoint:

```javascript
/v1/moves
/v1/people
```

```javascript
/v2/moves // breaking change
/v2/people // no change
```

Example backwards compatible changes:

- adding query parameters (they should always be optional)
- adding header or form parameters, as long as they are optional
- adding new fields in JSON or XML data structures, as long as they are optional
- adding endpoints, e.g. a new REST resource
- adding operations to an existing endpoint, e.g. when using SOAP
- adding optional fields to the request interfaces
- changing mandatory fields to optional fields in an existing API

Example incompatible changes (would require major version change):

- removing or changing data structures, i.e. by changing, removing, or redefining fields in the data structure
- removing fields from the request or response (as opposed to making it optional)
- changing a previously optional request field in the body or parameter into a mandatory field
- changing a previously required response field in the body or parameter into an optional field
- changing the URI of the API, such as hostname, port or path
- changing the structure or relationship between request or response fields, e.g. making an existing field a child of some other field
- adding a new mandatory field to the data structure

## Consequences

Releases of the API will be required to follow [semantic versioning](https://semver.org/) moving forward and unavoidable breaking
changes will need to be communicated in advance as part of these releases. With breaking changes we will
need to continue to support previous versions of the API.
