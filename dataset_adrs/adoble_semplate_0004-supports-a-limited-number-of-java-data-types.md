# Supports a limited number of Java data types

* Status: Accepted
* Date: 2021-02-18

## Context and Problem Statement

As the library will a) generate markdown text from Java objects and b) read in the markdown and generate Java objects, the data types need to be  converted to text and back again.
As not all data types can be implemented, what data types should be supported by the library?

## Considered Options

* A set of data type that are specific language agnostic
* Primitive Java data types
* Java wrappers for the primitive data types
* Java classes that are often used in documents
* Standard Java collections

## Decision Outcome

Data types that a native to Java are supported, i.e.:
* Primitive Java data types
* Java wrappers for the primitive data types
* Java Strings
* Java classes representing dates.
* Java classes representing URLs (for use in document links).

Using a language agnostic set of data type would provide extra complexity in translating from the Java data types and was rejected
