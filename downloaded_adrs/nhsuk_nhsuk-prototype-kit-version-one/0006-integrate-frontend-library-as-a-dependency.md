# 6/ Integrate frontend library as a dependency
**Author(s)**: Steven Adams   
**Status**: Accepted   
**Date**: 20th October 2017   

## Context
To speed up the prototype process it would be beneficial for the prototype kit to have generic styles available for consumers of the kit to use. This would also encourage more unified styling of prototypes and services to keep a feel of consistency across products.

## Decision
We will use the frontend library, available on the NHSUK GitHub, as a dependency. Using NPM (Node Package Manager) to pull in the contents of the repo and Gulp to move the files to the correct location and compile the assets. The version of the frontend library can be updated by changing the version number at the end of the following dependency in `package.json`:

```
"frontend-library": "git://github.com/nhsuk/frontend-library.git#0.6.0"
```

## Consequences
The frontend library is not currently well documented. This means that consumers will not know what components are available, and that they may have to reverse engineer the source code to figure out the correct DOM structure.
