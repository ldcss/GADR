# SQL Database schema - draft

* Status: In progress <!-- optional -->
* Deciders: James, Alli <!-- optional -->
* Date: 2019-07-16 <!-- [YYYY-MM-DD when the decision was last updated]  optional -->

<!-- Technical Story: [description | ticket/issue URL] optional -->

## Context and Problem Statement

<!-- [Describe the context and problem statement, e.g., in free form using two to three sentences. You may want to articulate the problem in form of a question.] -->

Replacing the sample JSON files with a fully-fledged database, to scale with the DPE app.

Building off of [the database schema ADR](https://github.com/bbc/digital-paper-edit-api/docs/ADR/2019-04-29-SQL-database-schema.md) - created via [DB Designer](https://dbdesigner.page.link/cq9FMHVVxsYqTasf7) - let's you export SQL code to Create and drop tables.

Deciding on RDS as a service and Postgres as an engine done [prior](https://github.com/bbc/digital-paper-edit-infrastructure/pull/9).

Things to decide:
* Whether to spin up local RDS instance for testing
* How to build up queries and DB logic, replacing JSON manipulation in routes
* How to handle migrations
* Seeding DB with existing JSON sample data to help development

## Considered Options

_TBC_
> Whether to spin up local RDS instance for testing

* Spinning up local psql server, adding env config for environments and switching to RDS on prod
* Dockerising local database setup
* Connecting to RDS locally

> How to build up queries and DB logic, replacing JSON manipulation in routes

* Manage raw SQL locally, connecting with `pg` (node-postgres package)
* Use an ORM such as Sequelize
* Use a thinner query-builder, such as Knex


## Decision Outcome

<!-- Chosen option: "[option 1]", because [justification. e.g., only option, which meets k.o. criterion decision driver | which resolves force force | … | comes out best (see below)]. -->
_TBC_

Option 3 was chosen as part of the spike and the fact that we have parameterised environments. This enabled speed for the spike with minimal overhead of extra Docker setup / db binaries.

Using `pg` in conjunction with `knex` allowed us to easily handle migrations and seeding with sample data. Found [Objection](https://vincit.github.io/objection.js/) and [Sequelize](http://docs.sequelizejs.com/) to be unnecessary for the queries we require. Objection is easily implementable later, if an ORM is required down the line.

<!-- ## Pros and Cons of the Options -->

<!--
### [option 1]

[example | description | pointer to more information | …]

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* …

### [option 2]

[example | description | pointer to more information | …]

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* …

### [option 3]

[example | description | pointer to more information | …]

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* …
-->

## Links
* https://medium.com/@jaeger.rob/seed-knex-postgresql-database-with-json-data-3677c6e7c9bc
* https://gist.github.com/NigelEarle/70db130cc040cc2868555b29a0278261
