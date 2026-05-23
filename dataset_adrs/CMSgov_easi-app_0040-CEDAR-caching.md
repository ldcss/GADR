# CEDAR Caching

**User Story:** [EASI-4129](https://jiraent.cms.gov/browse/EASI-4129)

EASi heavily relies on CEDAR core data for most system-centric and system profile views. However, CEDAR API responses can range from a few hundred milliseconds to multiple seconds, causing considerable wait times in the EASi application. As CEDAR relies on a low/no-code solution with limited caching options, we need to create a caching solution on our end to expedite calls to CEDAR for data.

A number of solutions listed below were considered. The main decision factors revolve around:

* Maintainability - will the solution be tenable into the foreseeable future?
* Scale - will the solution handle increased traffic to EASi and/or increased amounts of cached data?
* Development velocity - will the solution allow for the team to iterate quickly?

## Considered Alternatives

* Use in-memory caching already present within the EASi server app.
* Ask CEDAR to cache endpoints.
* Use a proxy server to cache requests (nginx).
* Use an optimized external key-value store to store data in lieu of making requests (Redis/Elasticache).

## Decision Outcome

We decided to move forward with implementing an nginx proxy server between our application and CEDAR. Since caching in nginx happens automatically, this choice requires the last amount of integration code while achieving the desired result. In addition, since it is almost entirely external to the EASi app, we can either shift to another approach or integrate other solutions easily in the future.

## Pros and Cons of the Alternatives

### Use in-memory caching already present within the EASi server app.

* `+` There's no additional architecture required.
* `+` One endpoint is already cached this way (system summary).
* `-` This would scale poorly as the cache is in-memory and is essentially a memory leak.
* `-` Would make debugging a production server more difficult as we would need to analyze the stack to determine if it's the cache or other code causing problems.

### Ask CEDAR to cache endpoints.

* `+` CEDAR can easily cache endpoints on their end and adjust cache time. No work required from the EASi team except for coordinating with CEDAR.
* `-` CEDAR has no ability to invalidate the cache on certain endpoints programmatically. This means certain endpoints would likely have to remain uncached or have a low cache time.

### Use a proxy server to cache requests (nginx).

POC can be found on the `EASI-4129/nginx-caching` branch ([link to PR](https://github.com/cms-enterprise/easi-app/pull/2545))

* `+` Once the proxy is set up, GET requests are cached automatically.
* `+` Nginx is very performant.
* `+` Requires the least amount of code to be written while still providing cache invalidation capabilities.
* `+` This solution is purpose-built for caching CEDAR, providing a clear philosophy of use.
* `+` The caching application is separate from EASi, making debugging and management easier.
* `+` Requests can be invalidate in a number of ways: sending a PURGE method to the same URL path, adding a query parameter, adding a path parameter, etc. The POC sends a PURGE method to accomplish cache invalidation.
* `-` The open-source version of nginx does not support caching natively, and a community module must be used. This requires a special Dockerfile to extend the main nginx image.

**NOTE:** We did also explore [Varnish](https://varnish-cache.org/) as an alternative to nginx as it supports cache purging natively, but unfortunately it does not support TLS meaning that [you would need a separate layer to handle HTTPS traffic](https://www.varnish-software.com/developers/tutorials/terminate-tls-varnish-hitch/). In light of this, we opted to just use nginx.

### Use an optimized external key-value store to store data in lieu of making requests (Redis/Elasticache).

POC can be found on the `EASI-4139/redis-caching` branch ([link to PR](https://github.com/cms-enterprise/easi-app/pull/2548))

* `+` Allows the most control over what to store and how to store it.
* `+` Can be used to store other values (cache DB queries, etc.).
* `+` Easily integrated with AWS and our current workflow using the official Redis Docker image.
* `+` Redis is very performant.
* `-` Requires writing code to retrieve/store every cached API call with the following additional considerations:
    * How do we manage keys?
    * How do we delete multiple values by key prefix?
* `-` Allows for storing other values outside of CEDAR responses. Introduces the possibility to bandaid slow DB queries by caching the data in Redis, for example.
* `-` Most expensive solution in terms of operating costs.
