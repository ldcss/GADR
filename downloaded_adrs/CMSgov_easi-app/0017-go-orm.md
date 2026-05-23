# Use [sqlx](https://github.com/jmoiron/sqlx) for Go Database Access

**User Story:** *[EASi 215](https://jiraent.cms.gov/browse/EASI-215)*

In order to save and access user data,
we need to use a database package.
This can vary from light standard libraries
to full featured ORMs.
This decision compares a few of those trade-offs
for the EASi application needs.

## Considered Alternatives

* *Use the [Go standard library](https://golang.org/pkg/database/sql/)*
* *Use sqlx*
* *Use [pop](https://github.com/gobuffalo/pop)*
* *Use [GORM](https://github.com/jinzhu/gorm)*

## Decision Outcome

* Chosen Alternative: *Use sqlx*
The main justification for using sqlx
is that other projects at Truss have used it with success.
Since Go doesn't have a mature ORM in comparison to other languages
(think Active Record in Rails),
their patterns are often outweighed
by the flexibility of sqlx.
Writing raw queries that get marshalled into Go structs
is the main use cases we're targeting,
and is what sqlx thrives at.

## Pros and Cons of the Alternatives <!-- optional -->

### *Go Standard Library*

* `+` No third party packages
* `-` No support for struct marshalling

### sqlx

* `+` Supports struct marshalling and embedded structs through joins
* `+` Typing sql allows us to optimize query performance
* `+` Typing sql allows flexibility with concurrency/locking
* `+` Good experience on other projects (eApp and saber)
* `-` Typing sql can be cumbersome and error prone
* `-` Joins/associations are manual

### *pop*

* `+` Association support
* `-` Performance issues in core utilities (such as n+1 joins)
* `-` Hides a lot of basic sql principles necessary
  for learning how to write queries (ex. transaction closures)
* `-` Raw queries are often necessary for complex joins or locking
* `-` Negative experience on past projects (MilMove)

### *GORM*

* `+` Most featured Go ORM (Associations, Transactions, Hooks)
* `+` Most widely used Go ORM (based on GitHub stats)
* `-` Would likely still end up writing a lot of raw sql
* `-` Some reports of similar performance issues to pop, such as n+1 queries
* `-` No prior project experience
