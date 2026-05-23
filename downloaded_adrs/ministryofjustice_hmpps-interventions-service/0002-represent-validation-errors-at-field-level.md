# 2. Represent validation errors at field level

Date: 2020-12-10

## Status

Accepted

## Context

For any user interface or client relying on our API, we need to define how we represent what was wrong with
invalid client requests.

## Decision

We will use field-level error validation.

We will use meaningful codes per field.

Example:
```json
{
  "status": 400,
  "error": "validation error",
  "message": "draft referral update invalid",
  "validationErrors": [
    {
      "field": "serviceUser.crn",
      "error": "FIELD_CANNOT_BE_CHANGED"
    }
  ]
}
```

## Consequences

All validation errors have to have corresponding codes assigned to them.

We have to document the expected error conditions in the OpenAPI specification.
