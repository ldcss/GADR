# Architecture Decision Records

## Summary

### Issue

We want a way of recording high-level technical decisions.

### Decision

Decided to use Architecture Decision Records (ADRs).

### Status

Accepted

## Detail

ADRs are markdown files, describing architectural-level decisions about the project.

See [https://github.com/joelparkerhenderson/architecture_decision_record](https://github.com/joelparkerhenderson/architecture_decision_record)

ADRs should be created for large decisions such as:

* Choice of database
* Choice of test framework
* Code structure
* CI/CD platform

ADRs should be agreed upon by core team members working on this codebase, with the agreement of the Principal Developers and Technical Architect where appropriate.

ADRs can be accepted before they are implemented, for example an ADR could be accepted to change to a new database before the development work has been started, or even planned.

When creating a new ADR, use the template in _documentation/ards/template.md
