# 0001: Namespacing TFL Types

## Context

TfL's Unified API has an extensive type system to describe the data returned from various endpoints.

In the OpenAPI Spec these follow a dotted naming convention to group related type definitions together.

See [the definition section of the OpenAPI file for reference](https://api.tfl.gov.uk/swagger/docs/v1).

Initially, the GraphQL types were all grouped together under the root `Type` module. This risked making the GraphQL implementation hard to follow as it didn't follow the organisation principles of the TfL API.

## Decision

`tfl-graphql` groups together GraphQL types into modules that closely map to the type definitions in the [Open API spec](https://api.tfl.gov.uk/swagger/docs/v1) for TfL's Unified API.

We ignore extra and unnecessary namespacing for example `Api.Presentation` when translating to Ruby modules.

This results in the following Open API Definition -> Ruby Module mappings.

| Open API Definition                            | Ruby Module                     |
| ---------------------------------------------- | ------------------------------- |
| `Tfl.Api.Presentation.Entities`                | `Tfl::Entities`                 |
| `Tfl.Api.Presentation.Entities.JourneyPlanner` | `Tfl::Entities::JourneyPlanner` |
| `Tfl.Api.Common`                               | `Tfl::Common`                   |
| `System`                                       | `Tfl::System`                   |
| `System.Data`                                  | `-`                             |
| `System.Data.Spatial`                          | `Tfl::System::Spatial`          |

Automated tests are also be organised into a directory structure that follows this namespacing approach.

We introduce a new namespace to encapsulate Enums used in the Api. `Tfl::Enums`.

## Status
Accepted

## Consequences

### Pros

- The project should be easier to maintain and understand for developers coming to the project. They should be able to mentally map the OpenAPI spec to GraphQL types.
- The root type space can be kept clean for base GraphQl types.
- The GraphQL type system can be extended without as much concern for naming collision.

### Cons

- Accessing deeply nested classes results in long module calls. e.g. `Tfl::Entities::JourneyPlanner::Journey`.
