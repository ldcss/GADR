# Use Flyway for Database Migration

We need a tool to handle database migrations
gracefully. We opt for Flyway, because while
other tools may be more comprehensive, they are also
more rigid and prone to failure.

## Considered Alternatives

* Flyway
* Fizz
* Golang-Migrate

## Decision Outcome

* Chosen Alternative: Flyway
* Flyway is a tried and true migration tool that is simple
yet effective. On our small project, a concise, easy to use
tool is most critical.

## Pros and Cons of the Alternatives

### Flyway

* `+` Simple to use
* `+` Effective (doesn't miss migrations)
* `+` Migrations written in SQL
* `-` Doesn't autogenerate models

### Golang-Migrate

* `+` Integrates with Go project
* `-` Ignores migrations committed out of order

### Fizz

* `+` Creates models for DB interfacing
* `-` Writing migrations in fizz language is more trouble than it's worth
