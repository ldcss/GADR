# Using Selectors and Reselect

## Status

Accepted

## Context

Using [selectors](https://medium.com/@matthew.holman/what-is-a-redux-selector-a517acee1fe8) is a best practice for Redux-applications to derive information from a minimal state while keeping the `mapStateToProps` and  `mapDispatchToProps` functions small.

I will use this pattern, because I made good experience with them on our work-project.
I am considering to use the [Reselect](https://github.com/reduxjs/reselect) for this, because it seems to be the "industry-standard".

Arguments for using Rselect:
- Reselect is very popular and has a lot of documentation on the official pages and on StackOverflow
- Reselect handles memoisation
- Adding reselect now is not much effort, because there are no selectors yet. Adding it later will require touching all selectors again.

Arguments against using Reselect:
- Selectors can also be written as plain functions to achieve the same separation of state and derived data
- An additional library adds to the size of the bundle
- The state of the tacboard is not that complicate, I don't expect memoisation to become a problem soon (but who knows?)
- Many of the selectors can not be cachedefficiently, because they depend on component-props (e.g. whether a field is empty or not requires the field-index), see [Reselect-Docs](https://github.com/reduxjs/reselect#accessing-react-props-in-selectors)

## Decision

I will use Reselect to rewrite the selectors. The only real downside seems to be the increased package-size, but that is not a big concern at this point.
It seems more important to avoid having to rewrite everything later. There also is a way to get memoization for selectors that use component props (see [Reselect-Docs](https://github.com/reduxjs/reselect#sharing-selectors-with-props-across-multiple-component-instances)).

## Consequences

I will rewrite the `mapStateToProps` methods for all components and move reusable logic into global selectors.