# ADR 0003: Domain-Driven Design

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)

## Context

During software development, the most common mistake is not speaking the same language with stakeholders and the product team. It is common having different points of view of the product architecture, and more significant gaps mean higher blockers and mistakes in the future.

Since we're creating a new product, we have the advantage of having the same language and architecture overview from day zero, meaning a more stable and robust infrastructure.

## Decision

To prevent these issues, we decided to implement the Design-driven Development framework to architect our domain collaboratively with the product team and business owners.

With DDD, we can ensure proper refactors in the future, having a clear overview of our entities' relationships and domains. To learn more about DDD, [check this summary](https://medium.com/@ruxijitianu/summary-of-the-domain-driven-design-concepts-9dd1a6f90091).

We can't have a clear, detailed overview of our entire domain structure (that would be overwhelming), but we've organized our DDD in a way that we can have a high-level concept of the whole company and drill-down to see a more detailed view of each bounded context.

**The high-level concept of our Domain-Driven Design** is located in this repository, at [ADR#0015](0015-model-overview.md). You can take a look at that record to learn more about our architecture overview.

**Bounded context detailed domains** are located in the same folder (`records/domains`), but there is a single file for each bounded context. Those architectures focus only on the given bounded context and any entity that relates to it.

Each microservice we have are related to a single bounded context. So, to create new microservices, you must add a new bounded context to our domain architecture.

## Status

Accepted.

## Consequences

Domain-Driven Design is not a common topic. We must teach our developers to use it. But, this effort may reward us well. A good, stable, and reliable domain architecture is the key to a successful company.

We must ensure our onboarding process covers this paradigm to avoid any unwanted unrelated domain entity.

---

## More reading

* [Brief DDD summary](https://medium.com/@ruxijitianu/summary-of-the-domain-driven-design-concepts-9dd1a6f90091) 
* [Book](https://www.amazon.com.br/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215/ref=asc_df_0321125215/?tag=googleshopp00-20&linkCode=df0&hvadid=379735814613&hvpos=&hvnetw=g&hvrand=12360278098423015108&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001751&hvtargid=pla-449269547899&psc=1)
