# Easily integrated with Java projects

* Status: Accepted
* Date: 2021-02-18

## Context and Problem Statement

`semplate` is intended to provide functionality to java developers so that they can build tools that create, use and/or manage documents that are written in markdown. As such, it should be easily to integrate it with programs written in Java.

## Considered Options

* Create as standard java JAR library
* Create as a microservice that can be called from a Java program (or programs that are written in other languages)


## Decision Outcome

Chosen option is to create as a standard Java JAR library

The option to create a microservice was rejected as these costs of hosting it could not be met. However, this option has not been excluded as additional to a standard Java JAR.  
