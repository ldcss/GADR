# 7. module.exports-vs-export-default

Date: 2019-08-26

## Status

2019-08-26 proposed
2019-08-27 rejected

## Context

When HapiJS plugins are registered they expect an object like this:

```JavaScript
{
  name: 'plugin-name',
  version: '1.0.0',
  register: (server, options) => {}
}
```

The problem with `export default` is that it exports an object whose property `default` is the value of the exported object. This makes my convention of having the `index.ts` register the plugin not work because HapiJS still uses CommonJs and won't get the `default` value E.g.

```JavaScript
import plugin from './plugin';

export default {
  plugin,
}
```

Switching between `module.exports` and `export default` will make using my packages tricky. It won't be clear when to use CommonJS or ES6 modules so I'll pick one and stick with it.

So let's use `module.exports` instead of `export default`.

## Decision

Rejected because if I try and import a module that uses `module.exports` Typescript shows an error that the file `is not a module`. The implication of this is that I have to replace [Glue][hapi-glue] to compose the API.

## Consequences

More rewrites.

[hapi-glue]: https://github.com/hapijs/glue
