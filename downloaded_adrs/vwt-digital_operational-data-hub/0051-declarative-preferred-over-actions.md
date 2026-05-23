# 51. Declarative preferred over actions

Date: 2020-09-21

## Status

Accepted

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

## Context

In computer science, declarative programming is a programming paradigm—a style of building the structure and elements of computer programs—that expresses the logic of a computation without describing its control flow.

Many languages that apply this style attempt to minimize or eliminate side effects by describing what the program must accomplish in terms of the problem domain, rather than describe how to accomplish it as a sequence of the programming language primitives (the how being left up to the language's implementation). This is in contrast with imperative programming, e.g. actions in Deployment Manager, which implements algorithms in explicit steps.

Declarative specifications are more clear on the expected result, once you are familair with the syntax. To understand the result of imperative specifications, interpretation of the statements in order of execution is required. Declarative syntax more explicitly states the result. Next to that, declarative specifications are context-independant. They state what should be there, instead of continuing on things that happened (or should have happened) before.

## Decision

We will prefer declarative syntax over imperative syntax.

## Consequences

### Advantages

Declarative syntax is more explicit in specifying what it wants to accomplish, compared to imperative specifications, which are context-dependant. Therefore, the result of declarative specifications is more consistent, as the context is not influencing the result. This leads to more predictable and more stable results.

### Disadvantages

Declarative syntax requires a domain specific language that needs to be understood, learned and maintained. Compared to using a imperative language that one might be familair with, it requires learning a new language. Each declarative language comes with its own tools, which need to be maintained and managed.

## References

* https://en.wikipedia.org/wiki/Declarative_programming, retrieved 3 November 2020
* https://ui.dev/imperative-vs-declarative-programming, retrieved 3 November 2020
