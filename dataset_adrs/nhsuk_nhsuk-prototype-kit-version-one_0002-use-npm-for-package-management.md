# 2/ Use NPM for package management
**Author(s)**: Steven Adams   
**Status**: Accepted    
**Date**: 29th August 2017

## Context
The prototype kit will need a way to consume the dependencies it requires to run. These will include think like getting the correct version of `Express`, the framework that prototype kit app is built on, and pulling in the correct version of the NHSUK UI kit assets.


## Decision
We will use NPM (Node Package Manager). Yarn, an alternative Node based package manager, when first released, had some benefits over NPM. These differences have now been implemented in the newer version NPM, Yarn and NPM are now interchangeable. The main benefit of NPM is that it comes packaged with Node.js and does not require an additional install like Yarn, removing a step from the setup process.

## Consequences
There is a dependency on consumers of the prototype kit to install a compatible version of Node.js with NPM on their machine.
