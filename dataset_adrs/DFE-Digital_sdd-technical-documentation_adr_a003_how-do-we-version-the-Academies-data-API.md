More info:
http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions

# Short title
How will we version our Academies data API (previously known as the TRAMS data API)?

# Status
CLOSED

# Context
Although we endeavour to make API changes backwards compatible, and such keep all clients on the same (shared) version of the API contract, there will be instances where this is not possible and a breaking change is required. Examples include: deprecating a route; correcting a typo; changing a data-type; re-organising the response schema to allow for metadata alongside the data requested.

When a breaking change is required we need a way to apply the change without breaking existing clients.

# Options
- Support multiple versions simultaneously from the same codebase, utilizing some data in the request to determine which version should process the request. Any piece of request data could be used, but we should use a common method for support: 
  - Specify a header in the request (e.g. `Accept: application/vnd.example.v2+json`)
  - Include a version number in the URL (e.g. `/v2/`)
- Support multiple versions simultaneously by running multiple versions of the code in production. Typically this approach would involve an additional component (an API Gateway) to route traffic to the correct back-end service.

There are further considerations depending on the option chosen.

# Decision

- To support a maximum of two simultaneous major versions from within the same codebase, utilizing the version number contained within the request URL.

We will proactively look to move clients to the most recent version and to make the previous version obsolete in order to simplify the codebase.

# Rationale

Given we have a small number of consumers at the moment, with the codebases within our control and within SDD, we can opt to keep only one previous major version at maximum.

There is not much between the URL vs. header versioning other than:
- it is more transparent to the developer what is happening when we version using the URL
- some integrations do not support setting custom headers, so we would be potentially limiting the future ability for others to use our API

The option to version using multiple simultaneous versions was not chosen as it is more complex in most areas, with the exception of the codebase within a branch:
- added infrastructural complexity and cost - additional components (API Gateway and previous version instance of API) add cost and complexity.  
- added branching strategy complexity - generally the ability to apply a 'hotfix' to old versions is desired, meaning a more complex branching strategy is required. Hotfixes would have to be applied to branches for each supported version.
- a hidden constraint exists - the need for database compatibility between the two versions, which is difficult to check for.


## Support for existing clients accessing versionless routes

Current API routes are versionless - these will be considered as version 1. We will also support addressing these routes with the `v1` prefix.

We shall start the versioning scheme at `v2`.

# Dependencies

A list of clients will need to be maintained, such that when we come to obsolete a route they can be given appropriate notice.

# Impact

As we need to maintain two versions within one branch, the codebase will grow in complexity. The effect of this should be reviewed within PRs and the use of mitigating coding patterns should be followed.

# Contributors

- Daniel Burnley
- Lewis Dale
- Robert McHugh
- Paulo Lanção
- Christopher Gunn

# Supporting Info (optional)

- [GDS Technical Standards](https://www.gov.uk/guidance/gds-api-technical-and-data-standards#when-iterating-your-api) - guidance on iterating your API, making backwards incompatible changes