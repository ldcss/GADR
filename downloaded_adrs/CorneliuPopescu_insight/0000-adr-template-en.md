# 0. Architectural Decision Record (ADR) template - english

Date: 2018-11-14

## Status

Proposed / Accepted / Declined / Superseded

Amended by [9. Help scripts](0009-help-scripts.md)

Amends [5. Help ](0005-help.md)

Superseded by [9. Help scripts](0009-help-scripts.md)

Supersedes [5. Help ](0005-help.md)

## Subject Matter Expert (SME)

Name of the person to ask about this decision

## Context

The tool will have a `help` subcommand to provide documentation for users.

It's nice to have usage documentation in the script files themselves, in comments.  When reading the code, that's the first place to look for information about how to run a script.

## Decision

Write usage documentation in comments in the source file.

Distinguish between documentation comments and normal comments. Documentation comments have two hash characters at the start of the line.

The `adr help` command can parse comments out from the script using the standard Unix tools `grep` and `cut`.

## Consequences

No need to maintain help text in a separate file.

Help text can easily be kept up to date as the script is edited.

There's no automated check that the help text is up to date. The tests do not work well as documentation for users, and the help text is not easily cross-checked against the code.

This won't work if any subcommands are not implemented as scripts that use '#' as a comment character.

## Dependencies

- NA

## References

- [Documenting Architecture Decisions](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)
- [ADR Tools](https://github.com/npryce/adr-tools)
- [ADR In Action](https://resources.sei.cmu.edu/asset_files/Presentation/2017_017_001_497746.pdf)
