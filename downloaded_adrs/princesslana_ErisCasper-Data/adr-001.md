# ADR-1: Code Generation

## Context

Serializing and deserializing JSON in Java works best when performing it to/from plain old java objects (POJOs).
While it is possible to serialize into generic `JsonNode` or `Map` objects this results in untyped values that
must be referenced via String keys, meaning the compiler is limited in what it can check for us.

The classes required for JSON serialization and deserialization are reptitive and error prone to write by hand.
[Immutables](https://immutables.github.io/) helps to some extent, but there are still many classes and fields to be written.

The [Discord API documentation](https://discordapp.com/developers/docs/intro) is mostly consistent with how it documents
the JSON structures it returns and accepts.

Code generation is often difficult to use with IDEs.
Code is often referring to classes that will not be committed, so we depend upon the IDE to generate these classes
so that the IDE can provide useful feedback regarding compilation errors.

## Decision

We will use code generation to generate the POJOs to be used for JSON serialization and deserialization.

We will generate classes that make use of Immutables.

## Consequences

The risk of errors when transcribing the Discord API are reduced.
The specifications can by copy/pasted directly from the documentation and used as the source for code generation.

By using Immutables we reduce the amount of code we must generate.
For example, Immutables provides us with
* implementations of `equals` and `hashCode`,
* a builder for each class, and
* code that is annotated for deserializing from and serializing to JSON.

Inconsistencies in the documentation format mean some manual changes are needed after copy/paste.
Care must be taken in managing these manual changes if (when) the Discord API is updated.

Using classes created by code generation using a custom script is not supported by IDEs. By isolating this code generation to its own library we avoid introducing friction when working with ErisCasper.java. This is in contrast to the code generation performed by Immutables that does have IDE support.
