# 3. Use superjson for serialising complex objects

Date: 2021-02-03

## Status

Proposed

## Context

The [Next.js docs on `getServerSideProps`](https://nextjs.org/docs/basic-features/data-fetching#getserversideprops-server-side-rendering) specify that objects returned from this function must be JSON serializable—this means only primitives, no complex objects or class instances.

Our gateways return domain models (instances of classes)—these cannot be directly serialized to JSON to be passed to the client side components.

We have a number of options:

1. provide methds on the domain classes to serialize and deserialize instances, then manually use these in our `getServerSideProps` functions and component definitions
2. return JSON response objects from our gateways and map them to domain objects in the components
3. use one of a number of third party libraries to do the serialisation for us

## Decision

Option 1 is reasonable, but would mean writing and maintaining more code that necessarily required.

Option 2 goes against our [principles](https://github.com/madetech/clean-architecture) and would litter our presentation components with boundary logic.

Therefore we have decided to use option 3: [`superjson`](https://github.com/blitz-js/superjson) was built for this explicit purpose and has a [Babel plugin](https://github.com/blitz-js/babel-plugin-superjson-next) which handles the serialisation and deserialisation for us implicitly, meaning our functions are clean from this logic.

## Consequences

We become dependent on a third party library for a key part of our system. This library is actively maintained and relied upon by the maintainers, we believe this is a safe choice.

The benefit of this change is that we're able to transparently use our domain models between server- and client-side without worrying about transport.
