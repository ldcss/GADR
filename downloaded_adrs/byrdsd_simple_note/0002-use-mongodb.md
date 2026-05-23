# 2. Use MongoDB

Date: 2020-08-06

## Status

Accepted

## Context

The app needs a database to store user data including authentication and notes.

## Decision

The app will use mongoDB for its database system, as its JSON-like structure is well-suited to the storage of simple text.

## Consequences

This will require using mongoid rather than active-admin, which breaks from standard Ruby.
