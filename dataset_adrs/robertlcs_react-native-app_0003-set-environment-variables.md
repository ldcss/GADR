# 3. Set environment variables

Date: 2018-09-01

## Status

Accepted

## Context

We need to set some APIs keys without publishing them on GitHub.

## Decision

We will add `config.js.example` and then explain in the README under a setup section that you need to copy that and call it `config.js` and add the secrets to it. `config.js` added to `.gitignore`.

## Consequences

We tried [babel-plugin-transform-inline-environment-variables](https://www.npmjs.com/package/babel-plugin-transform-inline-environment-variables) but it does not work proper with React Native (see an [issue](https://github.com/babel/minify/issues/687))
Another solution might be creating `config.js` and using like `import Config from './config.json'`.
You can also take a look at a thread about setting environment variables in Expo apps, maybe more interesting solutions will appear here in the future https://github.com/react-community/create-react-native-app/issues/57#issuecomment-298505228.
