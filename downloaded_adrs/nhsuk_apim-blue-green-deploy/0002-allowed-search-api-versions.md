# 2. Move the Search API Version from an environment variable to a code config value

Date: 2019-03-13

## Status

Accepted

## Context

The REST API for Azure Search requires the API Version identifier to be passed as the query parameter `api-version` for all calls<sup>[1]</sup>.

At the time of writing the General Available (GA) version is '2017-11-11' and the Preview version is '2017-11-11-Preview'. Attempting to retrieve an index definition for an index which includes Preview features with a query using the GA version in the query parameter `api-version` results in a HTTP error.

As a result of this we need to support the parametrisation and validation of the search API version. Validation could be against values held in environment variables or against config values within the code itself.

## Decision

* In order to maintain backwards compatibility the API Version identifier is an optional property in the payload. The default value is the current GA version.

* The validation will be based on config values **_**within**_** the code to check the api version parameter against a range of allowed values. The reason we have adopted this approach over using environment variables is that the code has been written to support specific versions of the API and therefore the responsibility for establishing this relationship rests with the code not the environment.

## Consequences

If a new version of the Search API is made available (either GA or Preview) then the supported versions check <sup>[2]</sup> will need to updated and tested to ensure that the code supports the new version. This in turn will require a release of the updated code.

[1]: https://docs.microsoft.com/en-us/rest/api/searchservice/
[2]: https://github.com/nhsuk/apim-blue-green-deploy/blob/master/lib/ValidateSearchApiVersion.js