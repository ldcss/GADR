# 1. Record architecture decisions

Date: 2019-05-09

## Status

Approved

## Context

We need to record the architectural decisions made on this project.

## Decision

We will use Architecture Decision Records, as [described by Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions).

## Consequences

See Michael Nygard's article, linked above. For a lightweight ADR toolset, see Nat Pryce's [adr-tools](https://github.com/npryce/adr-tools).

Use the `adr` command to manage ADRs.  Try running `adr help`.

ADRs are stored in a subdirectory of your project as Markdown files. 
The default directory is `doc/adr`, but you can specify the directory
when you initialise the ADR log.

1. Create an ADR directory in the root of your project:

        adr init doc/architecture/decisions

    This will create a directory named `doc/architecture/decisions' 
    containing the first ADR, which records that you are using ADRs
    to record architectural decisions and links to 
    [Michael Nygard's article on the subject][ADRs].

2. Create Architecture Decision Records

        adr new Implement as Unix shell scripts

    This will create a new, numbered ADR file and open it in your
    editor of choice (as specified by the VISUAL or EDITOR environment
    variable).

    To create a new ADR that supercedes a previous one (ADR 9, for example),
    use the -s option.

        adr new -s 9 Use Rust for performance-critical functionality

    This will create a new ADR file that is flagged as superceding
    ADR 9, and changes the status of ADR 9 to indicate that it is
    superceded by the new ADR.  It then opens the new ADR in your
    editor of choice.
    
3. For further information, use the built in help:

        adr help
