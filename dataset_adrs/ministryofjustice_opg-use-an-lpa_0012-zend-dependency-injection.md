# 12. Zend Dependency Injection

Date: 2019-05-01

## Status

Accepted

## Context

Zend Expressive allows us to pick from a number of Dependency Injection libraries.

The developers would specifically like to use a library that supports autowiring.

## Decision

To use [PHP-DI](http://php-di.org/). This was the only library that supported autowiring with no additional setup.

## Consequences

* We have autowiring!
* We can no longer use `initializers` from the Zend Service Manager
