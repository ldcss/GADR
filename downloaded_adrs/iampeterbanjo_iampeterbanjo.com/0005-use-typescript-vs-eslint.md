# 5. use-typescript-vs-eslint

Date: 2019-08-23

## Status

2019-08-23 done

## Context

Today I was trying to configure eslint to allow me to add "use strict" to my files. This project uses CommonJS modules which are not strict by default. I have several `.eslintrc.json` files in package folders which [behave correctly][eslint-folders] but I'm struggling to override the airbnb config in `./packages/server` to allow strict mode. If I used Typescript I would not need "use strict" mode, because it would be added by the compiler. And I could easily compose my `tsconfig` and `tslint` setup in the monorepo. I have tried using `@hapi/eslint-config-hapi` eslint settings but I'm not comfortable with that coding style. Creating my own custom eslint settings is one alternative.

The root cause of this is I thought strict mode was not necessary because of my misunderstanding of [ES modules][es-modules]. `require` is CommonJS, `import ... from` is ES modules.

Using Typescript:

### Pros

- Type checking
- Compile to target
- Sane configuration using base config and overriding in packages
- Compiler takes care of some linting
- Works really well with VS code
- Contemporary
- I have some types as js docs
- Works with [Cypress][cypress-ts]
- [ts-eslint][ts-eslint] combines best of both worlds
- Demonstrable use of Typescript
- Better VS code intellisense

### Cons

- Yet another thing to maintain - versions, types, compatibilty
- Not sure I need types everywhere
- Cannot be gradually adopted - in reality mixing js/ts doesn't work out well
- Code must be compiled or run with [`ts-node`][ts-node]
- Seperate commands to copy files into build folder
- Build times

## Decision

In the context of setting up this repo in strict mode. And facing the concern of being contempory, consistent use of types and lint rules let's adopt Typescript. I accept that there will be an initial work of conversion and some type wrangling.

## Consequences

- Maintaining type definitions
- Converting files to Typescript

[eslint-folders]: https://eslint.org/docs/user-guide/configuring#configuration-cascading-and-hierarchy
[ts-node]: https://www.npmjs.com/package/ts-node
[cypress-ts]: https://basarat.gitbooks.io/typescript/docs/testing/cypress.html
[ts-eslint]: https://github.com/typescript-eslint/typescript-eslint
[es-modules]: https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/
