# 1. ID Type

Date: 2018-06-24

## Status

Accepted

## Context

We need to decide what data structure to use as the identifier for domain entities.

## Decision

We will use a [GUID](https://msdn.microsoft.com/en-us/library/system.guid%28v=vs.110%29.aspx?f=255&MSPPError=-2147217396) type.

## Reason

In a distributed system, a simple integer type would not work. In case a database server was responsible for generating IDs, scaling the server out to multiple instances requires synchronization between them to ensure the same ID is not generated more than once.

GUIDs solve that problem because they are "unique" by definition with an acceptable collision rate. They can also be created by a client instead of requiring a centralized service.

The downside for GUIDs is that they take a lot of space relative to integers and also don't lend themselves well to indexing.

## Alternatives

Considering the distributed nature of the system, a [hi/low algorithm](https://vladmihalcea.com/the-hilo-algorithm/) or a [Twitter Snowflake algorithm](https://blog.twitter.com/engineering/en_us/a/2010/announcing-snowflake.html) would be viable solutions.