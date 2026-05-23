# 3. Use JUnit for tests instead of Spek

Date: 2017-11-01

## Status

Accepted

## Context

There are a number of unit testing frameworks available for the JVM.  There are also some newer unit testing frameworks that are specific to Kotlin.  Spring currently (4.x) only supports JUnit 4 and TestNG.  JUnit 5 can be made to work however.

## Decision

Use JUnit 5 for all unit and e2e tests.  This will simplify thing and has better integration currently with IntelliJ IDE.  

## Consequences

Spek is nice but doesn't work with Spring's integration yet.  As such, we'd have to write JUnit tests anyways.  The JUnit 5 integration is more of a POC but works w/ Spring 4.x.  Spring 5.x supports JUnit 5 out of the box.  

Tests will be a little more verbose, but JUnit supports nested tests and Kotlin allows for sentences for class and function names.  
