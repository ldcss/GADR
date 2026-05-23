# Use Go as CLI/Scripting Language

The EASi application
will require a set of command line utilities
to setup, test, and serve the application.
These scripts are executed
in local developer environments
and in the CI/CD pipeline.
Similar to the application itself,
these scripts require a language,
framework,
and organization patterns
to create and maintain their value.

In this ADR,
we'll decide what language and packages
will be used for writing scripts.
The main drivers for this decision
are ease of setup,
maintainability,
and developer adoption.

## Considered Alternatives

* *Go and standard library*
* *Go and [Cobra](https://github.com/spf13/cobra)*
* *Bash and Make*
* *Ruby/Python/other dynamic language*

## Decision Outcome

Chosen Alternative: *Go and Cobra*

Since Go is in the same language as the server application,
it should allow for a lower learning curve
and higher adoption among developers.
Many services we're looking to work with
(such as Docker, AWS, Postgres)
have Go packages that will help us write
develop a set of resources
that are more maintainable in the long term
than Make or Bash.
We're electing to add the Cobra library
because it offers substantial value
in its command line flag
and configuration packages.
The maintainability of Cobra style code
should outweighs the complexity of setting up a third party package.

We can mitigate some of the downsides of Go
by building out command execution helpers,
and using Go packages as opposed to executing to shell.

## Pros and Cons of the Alternatives

### *Go and standard library*

* `+` In the same language as the server application
* `+` Standardization around code style
* `+` Support for packaging/easier organization
* `+` Lower learning curve than bash
* `-` Verbose for scripting
* `-` Requires a package to run other command line tools
* `-` Flag and config support isn't great

### *Go and Cobra*

* `+` In the same language as the server application
* `+` Support for packaging/easier organization
* `+` More robust flag/config support than standard lib
* `+` Subcommand and flag syntax lend towards more sustainable code
* `-` Verbose for scripting
* `-` Requires a package to run other command line tools
* `-` Requires additional setup
* `-` Possible package lock

### *Make and Bash*

* `+` Shell command execution is native
* `+` Ubiquitous with scripting
* `-` Difficult to read syntax (subjective, but common)
* `-` Larger codebases can be hard to maintain

### *Ruby/Python/other dynamic language*

* `+` Lots of built in helpers for scripting
      (string manipulation, for/map/reduce shorthands, etc)
* `+` Support for packaging/easy organization
* `-` Learn another language
* `-` Setup another language
