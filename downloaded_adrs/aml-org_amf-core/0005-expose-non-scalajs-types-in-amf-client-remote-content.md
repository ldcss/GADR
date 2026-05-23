# 5. Expose non ScalaJS types in amf.client.remote.Content

Date: 2021-04-27

## Status

Accepted

## Context

To adopt the ScalaJSTypings plugin, usages of Scala types that were not exported to ScalaJS were removed from the scala interface.
The Api Designer product uses the `Content.stream` field and calls `toString()` on it. As this field is of type CharStream we hid
it from export.

## Decision

- Rollback the interface change for the `amf.client.remote.Content` class so that the `toString()` method can be called on the `stream` field.
- Add the `toString()` method in `Content` that returns the content in `stream`

## Consequences

The `stream` field is unusable besides the `toString()` method. Typings don't reflect that the field is exposed to avoid users using it.