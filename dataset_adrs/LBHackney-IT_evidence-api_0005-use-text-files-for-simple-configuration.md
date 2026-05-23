# 5. Use text files for simple configuration

Date: 2020-12-17

## Status

Accepted

## Context

There are certain pieces of configuration which do not change often but need to be easy to change for colleagues who are not developers. Some examples include:
- the document types that the API recognises and their metadata (like ther ID, title and description)
- the council services which the API recognises and their metadata (like their name and google group ID).

The choice came down to either storing these configurations in the database, or storing them in text files.

## Decision

Use text files for this configuration.

## Consequences

Benefits:
- Text files can be edited easily by anyone (even in place on Github)
- Reading a text file once is more performant than reading many times from a database for data which hardly changes

Drawbacks
- Changing the configuration requires a deployment—this was deemed acceptable due to the CI pipeline making deployments quick and automatic.
