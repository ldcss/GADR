# Discard Component Modules

* Status: accepted 
* Deciders: Gary Crye, Jamie Visker, Josh Gubler, Scott Hutchings
* Date: 2020-02-20

<!-- Technical Story: [description | ticket/issue URL] optional -->

## Context and Problem Statement

Terraform recommends not nesting modules into a deep hierarchy. We felt that varying from this recommendation made sense. We've started feeling some pain due to that decision. Do we follow this recommendation, or continue trying to organize modules for reusability and abstraction?

## Decision Drivers <!-- optional -->

* Terraform best practice
* Simplicity (maintenance, use, enhancement, fixes)
* Abstraction
* Reuse
* The way Terraform handles perceived changes to state

## Considered Options

* Keep using component modules 
* Discard component modules 

## Decision Outcome

Chosen option: "Discard component modules", the danger of breaking products and the pain of enhancement is too high with component modules.

<!-- ### Positive Consequences optional -->

<!-- * [e.g., improvement of quality attribute satisfaction, follow-up decisions required, …] -->

<!-- ### Negative Consequences optional -->

<!-- * [e.g., compromising quality attribute, follow-up decisions required, …] -->

## Pros and Cons of the Options <!-- optional -->

### Keep using component modules 

Standard modules compose component modules, which compose resources

* Good, because it's easier to propagate fixes.
* Good, because we get reuse of patterns (e.g. all the standards setup ALB the same way).
* Bad, because components have speculative complexity and/or don't meet the needs of other use cases.
* Bad, because discourages developers from really understanding their infrastructure components.
* Bad, because if a standard doesn't fit your need, the abstraction gets in your way of understanding the problem.
* Bad, because if a standard doesn't fit your need, you have to make lots of decisions (modify/copy standard, modify/copy component).
* Bad, because refactoring could create major breaking changes to the state files of many products.

### Discard component modules 

Standard modules compose resources

* Good, because module logic is focused on implementing the pattern (no speculative generic logic, seems more in line with DDD language design).
* Good, because it's easier to understand what the component actually builds.
* Bad, because all of the complexity is right there in front of you (need more/better comments).
* Good, because if the standard doesn't fit your need, it's easier to understand what it would take to modify the component.
* Good, because if the standard doesn't fit your need, it's easier to make the single decision of modify vs copy.
* Good, because without hierarchy, there is less refactoring that could break products.
* Bad, because logic will be duplicated among standards, making fixes harder to distribute.
* Bad, because logic will be duplicated among standards, allowing for more "drift".
* Bad, because this _is_ a major refactor that will cause products to have a major state change. Terraform will think it needs to tear down and rebuild a bunch of resources.
* Good, because _now_ is the time to do this kind of refactor, before we have a ton of products using the standards.


<!-- ## Links optional -->

<!-- * [Link type] [Link to ADR] example: Refined by [ADR-0005](0005-example.md) -->
<!-- * … numbers of links can vary -->
