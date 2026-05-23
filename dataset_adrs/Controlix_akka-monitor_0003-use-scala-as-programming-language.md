# 3. Use Scala as programming language

Date: 2018-06-01

## Status

Accepted

Amplified by [2. Use akka](0002-use-akka.md)

## Context

We have to decide on a programming language to write our API code.
Currently the team members are mostly familiar with _Java_ as a programming language. Therefor we might want to stick to _Java_ because then we do not have to learn a new language and we can focus on the new tools and the problem domain that we address.
However the support for _akka_ is much better in _Scala_. And we might also be eager to learn a new language.

## Decision

We will use _Scala_ to program the monitoring part of our application.

## Consequences

We have to learn a new language. That means there is a considerable overhead.
But the choice for _Scala_ facilitates the use of _akka_.
And it is nice to get to know a new language so we can use it in the future.
