# 59. Runtime dependency only on GCP

Date: 2020-10-15

## Status

Accepted

Implemented by [6. Implement Security by Design](0006-implement-security-by-design.md)

## Context

Availability of systems can be improved by reducing the number of dependencies. Each additional dependency comes with the risk of that service breaking, causing issues to our system. On the other hand, 3rd party services can be leveraged to quickly build and apply managed services at low cost, compared to creating and running these services by ourselves. Therefore, the right balance between dependency on and benefitting from external services is important.

During run the changes in 3rd party dependencies do not change. Therefore, caching or copying the functionality of these dependencies is possible in many cases. In build and development environments, the dependencies on 3rd party components and services change more often. Therefore, it is oftentimes not opportune to invest in becoming independent on these components and services.

## Decision

During runtime, we will only depend on resources services from the Google Cloud Platform.

## Consequences

Higher availability by not depending on 3rd party components and services during runtime, requires additional effort to cache or copy these dependencies.
Using 3rd party dependencies in build and development time introduces the risk of not being able to build or develop when these services are disturbed. However, by assessing the reliability to only select trustworthy parties this risk is acceptable.
