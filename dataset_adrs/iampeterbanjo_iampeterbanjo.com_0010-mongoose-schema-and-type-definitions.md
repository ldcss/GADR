# 10. mongoose-schema-and-type-definitions

Date: 2019-09-07

## Status

2019-09-07 proposed

## Context

I tried updating the schema for `RawTopTracks` to include the `importedDate` and discovered that I had to update quite a few files:

1. The Schema
2. The validators in the pipeline package
3. The tests for the validators and pipeline
4. The type definitions

It would be more convenient if the schema definition could also be used to generate the types and validate the inputs so that it would be easier to make changes. [Typegoose][typegoose-docs] seems to be something to explore. My concern is that I don't understand Typescript reflection and so Typegoose becomes a type of magic that will be difficult to debug and modify.

An alternative is to create classes in Typescript that [wrap the Mongoose schema][mongoose-schema-class]. This seems to be a more approachable solution.

## Decision

No decisions made.

## Consequences

No consequences.

[typegoose-docs]: https://hasezoey.github.io/typegoose/typedoc/
[mongoose-schema-class]: https://know-thy-code.com/mongoose-schemas-models-typescript/
