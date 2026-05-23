# 12. parallel-database-tests-mongodb-server

Date: 2019-09-15

## Status

2019-09-15 accepted

## Context

Jest tests are fast because they can be run in parallel. If we use the same database for every test, it can cause race conditions as multiple operations are performed on models and collections. There are two ways to decouple tests:

- [define databases in tests][defined-test-database]
- [randomly create databases for each test][random-test-database]

## Decision

In the context of database tests, and facing the concern of race conditions then create random databases for each test. There are different approaches for setting up the [test Mongodb server][test-mongodb-server] with Jest. I prefer using the `beforeAll` and `afterAll` hooks because this is more flexible and is less coupled to Jest's idiosyncracies.

## Consequences

- Slower first run as Mongodb test server is installed.
- Faster tests

[defined-test-database]: https://medium.com/@art.longbottom.jr/concurrent-testing-with-mongoose-and-jest-83a27ceb87ee
[random-test-database]: https://formidable.com/blog/2019/fast-node-testing-mongodb/
[test-mongodb-server]: https://github.com/nodkz/mongodb-memory-server
