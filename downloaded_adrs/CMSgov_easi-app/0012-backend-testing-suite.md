# Use Testify for Go Testing

The [Go standard library for testing](https://golang.org/pkg/testing/)
is pretty minimal.
It doesn't offer some key features that help organize tests, namely:
suite with setup/breakdown grouping
and common testing verbs, like `assert`.
This ADR focuses on picking a package
to alleviate some of those concerns in the EASI Go codebase.

## Considered Alternatives

* *Use the Standard Library Only*
* *Write Our Own Test Suite Package*
* *Use Testify*

## Decision Outcome

* Chosen Alternative: *Use Testify*
* Testify is a popular library
  and has been a helpful library on past projects.
  It offers the basics for suites and assertions,
  and the engineering team is already familiar with it.

## Pros and Cons of the Alternatives

### *Use the Standard Library Only*

* `+` No package imports or dependency locking
* `-` The impetus of this decision is that it's not featured enough.
      Building out those features would require lots of in-house code
      or redundancy.

### *Write Our Own Test Suite Package*

Similar to the above, except using DRY principles

* `+` No package imports or dependency locking.
* `-` Requires upfront work to build out features we want.

### *Use Testify*

* `+` Provides good suite/assert functionality out of the box.
* `+` Been tested on other projects.
* `-` Requires importing a package.
