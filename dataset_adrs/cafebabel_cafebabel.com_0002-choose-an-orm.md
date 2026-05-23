# 2. Choose an ORM

Date: 2017-11-02

## Status

Accepted

## Context

We need an ORM, especially to use Flask-Security.

Only 4 are available at the moment:

* Flask-SQLAlchemy: too bloated
* Flask-MongoEngine: relies on Mongo (harder migrations)
* Flask-Peewee: initial choice, not maintained anymore
* PonyORM: looks great but the code is hard to contribute to

## Decision

We will use Flask-MongoEngine and do migrations manually as of now.
We might want to find/code a tool for that in the future.

## Consequences

Inform the hosting company that we need MongoDB.

Update existing pull-requests.
