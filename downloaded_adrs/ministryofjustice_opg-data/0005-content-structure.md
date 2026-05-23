# 5. Content Structure

Date: 2020-01-27

## Status

Proposed

## Context

A consistent and well-defined document specification is required so that we may develop an API contract

## Decision

Our structure closely follows the [JSON-API](https://jsonapi.org/format/#document-structure) document structure

### Document Root Level

At the root level is always a JSON object.

This **MUST** contain at least one of the following root-level members:

* data: the document's "primary data" resource object
  * A single resource object is represented by a JSON object
  * A collection or resource objects is represented by an array of objects
* errors: an array of error objects

#### Single resource object

```json
{
    "data": {},
    "meta": {}
}
```

#### Collection of resource objects

```json
{
    "data": [
        {...},
        {...}
    ],
    "errors": [],
    "meta": {},
    "links": {}
}
```

JSON-API states

> The members data and errors MUST NOT coexist in the same document.

`opg-data` standard is that if a data resource OBJECT is returned, then there **MUST be no** error member.

However there ARE certain circumstances where an array of errors **MAY** be returned alongside a data resource COLLECTION. See [0007-error-handling-and-status-codes.md#errors-in-20x](0007-error-handling-and-status-codes.md#errors-in-20x)

The root JSON object **MAY** also contain the following root-level members:

* meta: a meta object that contains non-standard meta-information
* links: a links object related to the primary data (typically used for pagination links if the data returned is a collection)

### The Resource Object

See [JSON-AP](https://jsonapi.org/format/#document-resource-objects)

Namely:

* As a minimum, every resource object **MUST** contain:
  * an id member
  * a type member. The values of the id and type members **MUST** be strings. For consistency and the avoidance of confusion, types **MUST** use PLURAL. eg "articles", "people"
  * an array of attributes (even if empty)
* IF the "data" top level member is present, then there **MUST** be a `links` array, containing as it's minimum, a `self` member with a URL which **MUST** be callable at the API
* A resource object's data attributes is presented in an array named "attributes"
* A resource object's links is presented in an object named "links"
* A resource object's relationships is presented in an array named "relationships"
* A resource object's attributes and its relationships are collectively called its "fields"

```json
{
    "data": [
        {
            "type": "articles",
            "id": "1",
            "attributes": {
                "title": "My First Article",
                "description": "..."
            },
            "links": {
                "self": "https://api.example.com/articles/1",
                "next": "https://api.example.com/articles/2"
            },
            "relationships": {
                ...
            }
        },
        {
            "type": "articles",
            "id": "2",
            "attributes": {
                "title": "Second Article",
                "description": "..."
            },
            "links": {
                "self": "https://api.example.com/articles/2",
                "prev": "https://api.example.com/articles/1"
            },
            "relationships": {
                ...
            }
        }
    ],
    "links": {},
    "meta": {}
}
```

#### Relationships

Relationships will be defined in a separate ADR

### Meta

See [JSON-API](https://jsonapi.org/format/#document-meta)

### Errors

Errors responses will be defined in a separate ADR

## Consequences

A consistent and well-defined specification
