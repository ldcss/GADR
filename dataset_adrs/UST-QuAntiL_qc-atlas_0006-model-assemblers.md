# Use model assemblers for HATEOAS responses 

* Status: accepted
* Deciders: [QuAntiL EnPro Team]

## Context and Problem Statement

Spring HATEOAS includes several classes that encapsulate domain objects, adding support for links.
Constructing such objects, as well as adding the desired links to them is a common operation that
requires entity-specific boilerplate code.
How can duplicate code in nearly all controller methods be avoided? 

## Decision Drivers <!-- optional -->

* Avoid duplicate code to create HATEOAS models
* Decouple link creation from normal entity logic

## Considered Options

* Make links part of the entity objects and use inheritance
* Separate model assembler classes

## Decision Outcome

Separate model assemblers were chosen, as the former option would require us to have a deep coupling between HATEOAS types
and our DTO classes.

Due to the assembler classes being initially only used for links they all reside in the `linkassembler` package.

## Pros and Cons of the Options

### Make links part of the entity objects and use inheritance

* Good: easy to implement
* Bad: Deep coupling between Spring HATEOAS internals and our types

### Separate model assembler classes

* Good: Clear separation of concerns
* Bad: More complex implementation, especially if call sites are to be kept short
