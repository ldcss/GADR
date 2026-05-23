# 5. Avoid short variable names

Date: 2020-06-29

## Status

Accepted

## Context

Idiomatic Go calls for "short, descriptive" variable names, which is fine, but I abhor needlessly short variable names.  
Code is for humans to read and understand. Having single character variable names is rarely helpful. Reducing the cognitive load on software engineers trying to understand what code is doing should be one of the top priorities of any shared codebase.

## Decision

In this project, single character variable names will typically only be used for temporary loop variables (e.g. i, j for indexes).  Variable names will be as short as possible but not at the cost of not being descriptive enough.  Exceptions are fine.

## Consequences

There will be exceptions to this rule. I have already run into a case where I want to use a simple variable name, but the linter warns me it clashes with a package name.  So it might be difficult or impossible at times to obey this rule.  
It will be interesting to me if I start to use abbreviated variable names and then later revert this ADR! 
