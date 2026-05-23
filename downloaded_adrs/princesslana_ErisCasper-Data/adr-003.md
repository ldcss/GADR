# ADR 3: Nullable Class

## Context

Fields in the JSON structures used by the Discord API can be optional, nullable, or both
(see [here](https://discordapp.com/developers/docs/reference#nullable-and-optional-resource-fields)).
This means that we can not treat `Optional.empty()` and `null` the same.

Adding a `@Nullable` annotation to an `Optional<T>` field is not handled well by Immutables.
It will not generate the methods need to make using such a field in a builder 'nice'.

Immutables supports [custom encodings](https://immutables.github.io/encoding.html) for types.
It does not allow detecting the encoding to use via annotation.
It requires that the encoding be compiled before the main compilation stage.

## Decision

We will create a `Nullable<T>` class, similar in functionality to `Optional<T>`.

We will create an encoding for that class, making the builder easier to use for
fields of that type.

## Consequences

Using the encoding requires two passes at compilation.
First to compile the encoding, followed by the main pass that will make use of the encoding.

A `Nullable<T>` class is a little unusual (most intuitive would be to allow `null`).
But, it would also be confusing to have `Optional<T>` fields that could be set to `null`.
