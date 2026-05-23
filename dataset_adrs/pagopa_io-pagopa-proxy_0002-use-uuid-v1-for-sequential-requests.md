# 2. Use uuid/v1 for sequential requests

Date: 2018-05-21

## Status

Accepted

## Context

We have to send requests to a server that requires unique Request IDs for each message.
So, we need to generate uuids.

## Decision

We decided to use uuid library and generate unique uuids based on timestamp (Version 1):
https://www.npmjs.com/package/uuid


## Consequences

Each request should use unique uuid, avoiding collisions.
