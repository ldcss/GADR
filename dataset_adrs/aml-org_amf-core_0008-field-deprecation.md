# 8. Field deprecation

Date: 2021-09-20

## Status

Accepted

## Context

We need to start deprecating old fields and have no mechanism to do so.

## Decision

We will start deprecating fields. Getter/setter methods in Scala and Platform classes will be deprecated also. Deprecated fields will still be set alongside new fields until these are removed in the next major version. 

How to deprecate a field:
1. Deprecate field definition in model class
   1. Deprecate field definition with `@deprecated` annotation
   2. Deprecate field definition with the `deprecated=true` paramter from the `Field` class
   3. Annotate the `fields` value assignment with `@silent("deprecated")` annotation to avoid compilation errors from deprecated fields
2. Deprecate getter/setter methods in Scala and Platform classes with `@deprecated` annotation
3. Update usages of getter/setter methods to use both legacy and new fields (with the `@silent("deprecated")` annotation)

## Consequences

* The `@silent("deprecated")` annotation should be used to discard compilation errors from the use of deprecated methods. Note this annotation **can only be used in assignment expressions**
* We will have "trash" code setting the legacy fields, just for the sake of backwards compatibility
* No migration from old fields to new fields are provided. Only when parsing a "YAML Spec" (API, Dialect, Dialect Instance, etc.) both the legacy and new fields will be set.
