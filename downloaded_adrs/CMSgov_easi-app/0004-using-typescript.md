# Using Typescript

- Status: Proposed [Proposed, Accepted, Rejected, Deprecated, Superseded, etc.]
- Deciders: Mikena, Eady, Chris
- Date: 2019-10-17

Traditionally, JavaScript has been the preferred language for client-side
development. However, recently Typescript, a superset of JavaScript, has
gained popularity and is a language we wanted to learn more about.

## Considered Options

- JavaScript
- JavaScript w/ [Flow](https://flow.org)
- [Typescript](https://www.typescriptlang.org/)

## Decision Outcome

Typescript

- `+` Strong static typing system will help reduce possibility of bugs at
  runtime, Errors are captured at compile time.
- `+` Typescript has overlapping
  [object oriented concepts](https://levelup.gitconnected.com/typescript-object-oriented-concepts-in-a-nutshell-cb2fdeeffe6e)
  to a deeper level than
  [ES6 classes](https://www.sitepoint.com/object-oriented-javascript-deep-dive-es6-classes/)
  and traditional JavaScript.
- `+` Code is clearer and easier to understand with
  [static typing](https://www.typescriptlang.org/docs/handbook/basic-types.html)
  and [interfaces](https://www.typescriptlang.org/docs/handbook/interfaces.html).
- `+` Does not require any additional setup (assuming we use
  [Create React App](https://github.com/facebook/create-react-app))
- `+` Typescript has many helpful autocomplete and snippet generation features
  that make development faster.
- `-` Adds a layer of complexity which will initially decrease productivity
  to get on-boarded

More information about Typescript
and how it will aid our frontend development
using React can be found
[here](https://www.pluralsight.com/guides/composing-react-components-with-typescript)
and
[here](https://fettblog.eu/typescript-react/).

## Pros and Cons of the Alternatives

JavaScript

- `+` No additional on-boarding or learning required.
- `+` JavaScript has much heavier usage and community support compared to Typescript.
- `-` No static typing

JavaScript w/Flow

- `+` Very similar to JavaScript with special sauce
- `-` Have had negative experience with unclear error messages and limited
  support
- `-` Reported issues of sluggish activity across IDE/editors hogging
  bandwidth on machine's (YMMV)
- `-` Requires a flow declaration (`// @flow`) at the top of every file
