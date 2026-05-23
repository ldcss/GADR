# 6. monorepo-dependencies

Date: 2019-08-24

## Status

2019-08-24 accepted

## Context

I'm trying to make changes to this monorepo but I keep encountering dependency problems. Ideally the root package.json contains the devDependencies allow the `packages/` folder's package.json to contain the dependecies. This works reasonably well with yarn, lerna or pnpm but using npm I see errors like:

```shell
> site@1.0.0 lint /home/iampeterbanjo/clever-cloud/iampeterbanjo.com
> npx eslint "**/*.{ts,js}" --fix

Cannot read config file: /home/iampeterbanjo/clever-cloud/iampeterbanjo.com/node_modules/@typescript-eslint/eslint-plugin/dist/index.js
Error: Cannot find module 'typescript'
Referenced from: /home/iampeterbanjo/clever-cloud/iampeterbanjo.com/packages/server/.eslintrc.json
```

Packages that could be shared:

- Typescript
- Eslint
- Prettier

It is possible to share configurations from a base config with Typescript. e.g.

```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./build"
  },
  "include": ["src", "__tests__"]
}
```

For prettier I can publish my [custom configuration][published-prettier-config] and reference it in `package.json` like:

```json
{
  "name": "my-cool-library",
  "version": "9000.0.1",
  "prettier": "@company/prettier-config"
}
```

## Decision

- All packages should contain all their dependencies.
- The root `package.json` contains only convenience scripts or base configs.
- Drop eslint because it's value is not clear: prettier formats, Typescript checks - done.

## Consequences

- Installation times could get longer
- More `node_modules` means more disk space used
- Simpler dependency structure
- Dropping eslint simplifies formatting

[published-prettier-config]: https://github.com/azz/prettier-config
