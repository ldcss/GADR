# 15. Library for application forms

Date: 2019-05-09

## Status

Accepted

## Context

We want to use a common library for managing HTML forms used within the service. 

Two libraries were investigated; Zend Form and Symfony Forms.

## Decision

We will use Zend Form.

## Consequences

* Zend Form required less boilerplate code. The end result being more expressive within the handles.
    * This also simplified testing.
* Better compatibility with Zend's CSRF middleware.
* We don't get the benefit of some view helpers that were available via Symfony Forms.
