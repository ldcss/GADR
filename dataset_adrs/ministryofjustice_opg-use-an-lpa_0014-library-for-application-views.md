# 14. Library for application views

Date: 2019-05-09

## Status

Accepted

## Context

We need to use a common library for managing HTML views within the service.

Two libraries were investigated; Plates and Twig.

## Decision

To use Twig.

## Consequences

* We get auto-escaping.
* It aligns with the LPA Online Tool service.
* It prevents native PHP being included in the template.
    * This offers an extra layer of protection.
    * But removes a level of flexibility.
* It doesn't align with the Refunds Service.
