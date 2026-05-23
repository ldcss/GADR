# ADR 006: DataTypeInfo provision

## TL;DR

Search will provide a single DataType which will be loaded on construction. DataTypeInfoProvider will be removed. SearchRegistry will provide access to DataType as part of a Search.

## Context

Adding field info and carrying out array flattening requires access to DataTypeInfo for primary and linked searches.

The current implementation uses instances of JsonDataTypeProvider which read multiple types from a single file. This would mean lots of duplication between different searches.

Each search needs to expose the correct data type, as it will provide a single data type now, albeit with multiple targets.

## Decision

The situation can be greatly simplified, with the following changes:
* Search provides a single DataTypeInfo which is passed on construction
* DataTypeInfo has methods for building from JSON or a JSON resource
* DataTypeInfoRegistry and implementing classes become unnecessary
* SearchRegistry provides access to list of Searches, and hence DataTypes, for use in result decoration/array flattening

## Status
Beta

## Consequences
InfoService will need to be reworked and possibly a top-level info service provided to give access to lists of endpoints and data types etc

## Tags
