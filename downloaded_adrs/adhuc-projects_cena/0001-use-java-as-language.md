# 1. Use Java as language

Date: 2018-12-27

## Status

Accepted

## Context

We need to choose a programming language to implement the `menu-generation` application.

`menu-generation` application will be developed initially during the author's free time, thus this time is limited.
Development may involve other developers in the future, and the chosen language should not restrict participation.

## Decision

Java is a broadly used programming language, and the most well mastered one by the author. Thus Java will be the
programming language used to implement the `menu-generation` application.

## Consequences

Usage of Java as the programming language will speed up implementation. It may also help open-source community to
collaborate with the author.

Usage of Java therefore implies usage of object-oriented programming paradigm.

`menu-generation` application will define a `org.adhuc.cena.menu` base package to contain its source code.

Other programming languages running on the JVM may be introduced during implementation, sharing the same libraries as
the ones used in the Java implementation.
