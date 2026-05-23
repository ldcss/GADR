# Pull acs-info out of modules

* Status: accepted 
* Deciders: Gary Crye, Jamie Visker, Josh Gubler, Scott Hutchings
* Date: 2020-02-20

<!-- Technical Story: [description | ticket/issue URL] optional -->

## Context and Problem Statement

Using acs-info inside our standard and component modules is creating pain. Does it make more sense to expect products to pass the necessary variables in, allowing them to use acs-info if they want?

## Decision Drivers <!-- optional -->

* Terraform's lack of optimization with modules and data sources
* Usage of modules in non-OIT accounts
* We want our modules to be simple to use
* We want development teams to understand the infrastructure of their products.

## Considered Options

* Pull acs-info out of modules
* Leave acs-info in modules

## Decision Outcome

Chosen option: "Pull acs-info out of modules", because it was the best option based on an analysis of pros and cons (see below).

<!-- ### Positive Consequences optional -->

<!-- * TBD -->

<!-- ### Negative Consequences optional -->

<!-- * TBD -->

## Pros and Cons of the Options <!-- optional -->

### Pull acs-info out of modules

Any needed account information will be passed in via input variables. Products can obtain this information any way they choose (acs-info, query SSM, other data source, hard coded, etc.).

* Good, because encourages our modules to be account agnostic.
* Good, because we aren't making a bunch of API calls to fetch data we don't need.
* Good, because modules will be more stable.
* Good, because we aren't instantiating multiple instances of acs-info.
* Bad, because products have to find information needed by modules.
* Bad, because products might need to understand what is happening inside the module to know what value is appropriate.

### Leave acs-info in standard modules

This is what we are currently doing.

* Good, because the contract for using the standard modules is simpler.
* Bad, because when acs-info breaks, the product is not empowered to workaround the issue.
* Bad, because acs-info fetches a bunch of unneeded info.
* Bad, because multiple standard modules instantiate multiple copies of acs-info.
* Bad, because the products often need acs-info anyways (we don't have standard modules for everything; often the product composes raw resources alongside standards).

<!-- ## Links optional -->

<!-- * [Link type] [Link to ADR] example: Refined by [ADR-0005](0005-example.md) -->
