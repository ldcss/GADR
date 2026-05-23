# 4. Use Yarn

Date: 2020-10-21

## Status

Accepted

## Context

NPM is causing confusion as to why lock files are changing in local
environments when no changes have been made. We have found explanations and
workarounds, but it feels like the type of unexpected default behavior that will
lead to frustration as new developers join the project.

Yarn is an alternative package manager that seems to have a more expected set
of default behaviors while maintaining compatibility in case we need to revert.

## Decision

We will use Yarn instead of NPM for this project.

## Consequences

We will be more confident we have repeatable builds across environments as the
issues we've seen with inconsistent lock files will go away.

We will be able to focus on developing the application instead of spending time
learning the odd behaviors of a package manager and when workarounds are
expected as default behavior.
