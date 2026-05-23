# 5. read model tables

Date: 2018-06-09

## Status

Accepted

## Context

Querying dynamodb requires a hash key.

 > in order to query dynamodb, you need at least to query on your 'hash' key, and you will get ordered results on your range key (if you have range key)

from [StackOverflow](https://stackoverflow.com/a/34463999/222163)

So it isn't possible to have a `FooReadModel` table and read the most recent items from it.

## Decision

Instead of a `FooReadModel` table there will be a `ReadModel` table that any readmodel is written too. It will have a `type` as a hash key and a timestamp as a range key.

## Consequences

 * All consumers of streams of readmodels will need to know the type of the readmodel as well as the dynamodb location
 * ReadModels in dynamodb can be queried by `type` and will be returned in `timestamp` order
