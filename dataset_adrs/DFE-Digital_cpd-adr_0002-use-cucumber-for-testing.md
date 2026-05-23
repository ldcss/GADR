# 2. Use Cucumber for testing

Date: 2021-03-18

## Status

Accepted

## Context

* Dev team discussion over what level to write tests at and the trade-offs involved.
* Discussion over existing cucumber PR https://github.com/DFE-Digital/early-careers-framework/pull/151/files
* We already have cypress.io tests in place and are currently working out the best approaches.
* There is an overhead writing matchers for cucumber.
* It is repeatedly useful having a description of the flows in the system:
	* To share with accessibility (a11y) testers
	* To share with security/penetration testers
	* To share (and possibly edit) with/by non-coder team-members such as Business Analysts and our cross-team testing expert.
* Details of exactly what to put in gherkin syntax files and what to put in pure code tests will require some judgement.
* Consistency across the several projects involved is valued as some people are working across all of these projects.

## Decision

* Use cucumber to describe all flows that are of significance to the business, notably the "happy paths".
* Use pull request reviews to refine exactly what to put in gherkin files versus pure-code tests.

## Consequences

> "What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated."

* Using matcher syntax will add overhead to test writing.
* We expect that the benefits of having a (non-technical) human description of the platforms will outweigh the development burden.
