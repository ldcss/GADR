# 2. Adopt DDD approach

Date: 2018-12-27

## Status

Accepted

## Context

`menu-generation` application's scope is not well defined and may cover a lot of concepts around the Menu generation
features, such as:

- managing a recipes catalog
- searching in this catalog for recipes based on multiple criteria
- collaborating on this catalog
- handling allergies and tastes
- generating shopping lists

All above concepts may be complex to model and should not be considered as simple data in a CRUD system. Other new
features may emerge in the future. In addition, all those features are related but should not be treated as a whole in
a big ball of mud architecture.

## Decision

[Domain-driven design](https://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) as defined by
Eric Evans will help modeling the different concepts managed by the `menu-generation` application, keep the ability to
adapt the model based on new insights and split the whole application into different bounded contexts to avoid mixing
those concepts in one giant messy code base.

## Consequences

The emphasis will be put on domain modeling, consisting on aggregates and services, and object-oriented programming will
help designing the underlying domain objects. The domain objects must be kept as agnostic of the infrastructure
implementation as possible to avoid mixing concerns and complicating modeling activity.

Each aggregate will be isolated in a dedicated package, consisting of the aggregate class itself and all its related
components (i.e. entities and value objects), plus domain and application services. Packages won't depend on any
implementation framework, and will depend on other aggregate packages only if a relation exists between those aggregates,
in an unidirectional dependency graph, to avoid cyclic dependencies.

During development, different bounded contexts will emerge, encapsulating their own domain concepts. That may result
in splitting the application into different modules or services.
