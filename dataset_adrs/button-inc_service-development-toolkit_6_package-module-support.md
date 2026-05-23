# Design Decision 6 - Package Module Support

## Background

Decision to support different module imports

## Findings

We Considered the following to support:

| CommonJS                                                                                                       | ES Modules                                                                                                                                                                 | UMD                                                                                               | AMD                                                      |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| CommonJS supports nodejs and webpack. Server-side rendering applications using node can be used with commonJS. | ES modules [offer support for tree-shaking](https://webpack.js.org/guides/tree-shaking/#conclusion), support tools like webpack and rollup, and are usable in the browser. | Universal module supporting both client and server. Can be used as a fallback module for webpack. | Imports modules asynchronously for use on the front-end. |

Popular component libraries were also researched for common support types in use, including react-bootsrap and semantic-ui react.

## Resources

- https://blog.harveydelaney.com/creating-your-own-react-component-library/
- https://webpack.js.org
- https://github.com/react-bootstrap/react-bootstrap
- https://react.semantic-ui.com/

## Decision

In order to offer broad support for different application types, decision was made to compile into commonJS, ES modules, and UMD. As use cases for AMD, such asynchronous imports and client support are covered by UMD or ESM, and it has less popular demand, we have decided not to support it.
