# 11. Moving forward Forms API will not be used to create/update concepts

Date: 2018-05-18

## Status

Accepted

## Context

Concepts can be created/updated using Concepts API or along with FormElement through Forms API.
This doubles the test cases and increases maintanence.

We consistently saw bugs in Forms API when creating or updating coded concepts along with it.

## Decision

We will create Concepts through Concepts API. Forms API will refer concepts.

## Consequences

All implementations' Forms/Concepts need to be restructured. Concept create/update branch needs to be removed from Forms API.
