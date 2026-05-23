# 5. Use Storybook to build self contained components, but not for UIs

Date: 2019-02-07

## Status

Accepted

## Context

We need a workflow to build our appliation and components.

## Decision

We use Storybook only for building new self contained components.

## Consequences

because this allows us to define the different state of the components, and then develop isolated on them without the need to build a complete app around them. We have to make sure we don't use it to build UIs because this is better done with UI frameworks that allready include components that are then extended by our own components. 


## Links

* https://dzone.com/articles/practical-guide-to-storybook-driven-development
* https://blog.hichroma.com/the-delightful-storybook-workflow-b322b76fd07