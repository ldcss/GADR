# 0002: Using JSON Schema in Specs

## Context

GraphQL recommends [testing the behaviour of a GraphQL API from the client's perspective](https://graphql-ruby.org/testing/integration_tests.html).

We need to test that the data returned from GraphQL queries conforms to the type definition system.

### Option explored

1. Individual expectations

For example validating each key in a response.

```ruby
expect(response).to include('id')
expect(response).to include('commonName')
expect(response).to include('stops)
```

2. FactoryBot

This potentially could be achieved using [FactoryBot](https://github.com/thoughtbot/factory_bot). However validating against dynamic GraphQL queries may not be possible. For example if we wanted to test that a GraphQL query can return just one key from a type AND test the same query can return multiple keys.

In testing GraphQL responses, we are primarily interesting in the shape and structure of data and not really the content.

3. JSONSchema

JSONSchema provides a declarative domain specific language to define and validate the schema for JSON objects. Furthermore, it allows us to define a JSON schema and test conformity.

## Decision

`tfl-graphql` uses [JSON Schema](https://json-schema.org/understanding-json-schema/) validation to test responses from GraphQL queries.

It implements a [custom RSpec Matcher](/spec/support/schema_matcher.rb) based on [this article from Thoughtbot](https://thoughtbot.com/blog/validating-json-schemas-with-an-rspec-matcher).

This matches a given object against schema defined in `spec/schemas`.

## Status

Accepted

## Consequences

### Pros

- We can now dynammically test schemas conform to GraphQL type definitions.
- Our RSpec expectations for schema validation can be short one liners using the `matches_response_schema(schema_path)` matcher.
- We have valid JSON schema that could be reused for other purposes if we need them.

### Cons

- There is extra work needed to define the JSON Schema we expect from GraphQL queries. Longer term we could explore automatically generating these schema, perhaps by consuming the OpenAPI spec.
