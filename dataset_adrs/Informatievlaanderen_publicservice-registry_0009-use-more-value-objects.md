# 9. Use Value objects as much as possible.

Date: 2017-09-12

## Status

Accepted

## Context

A value object is a small object that represents a simple entity whose equality is not based on identity: i.e. two value objects are equal when they have the same value, not necessarily being the same object. Examples of value objects are objects representing an amount of money or a date range.

In `Wegwijs`, we experienced great value towards type safety from using VOs. We want to bank in even more on the use of VOs.

## Decision

Use a Value Object wherever possible.

## Consequences

More type safety.

A more expressive domain.

Sensible code reuse.
