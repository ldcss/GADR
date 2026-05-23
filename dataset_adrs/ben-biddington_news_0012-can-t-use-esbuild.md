# 12. Can't use esbuild

Date: 2021-06-13

## Status

Accepted

## Context

Had a go with `esbuild`, and it *is* very fast, but we can't use yet due to runtime failures in the browser.

> 'Dynamic require of "http" is not supported'

Which stems from our usage of `rss-parser` in `src/adapters/rss/feed.ts`.

### Tips

Our current `esbuild` fails at runtime, but we alse needed to resolve a couple of problems to get the build itself to work.

We ended up with:

```
./node_modules/.bin/esbuild ./src/adapters/application/real-application.js\
  --external:http --external:https --external:timers\
  --bundle --global-name=real --outfile=./src/adapters/web/gui/assets/dist/real.bundle.js 
```

Which resolves the following issues.

#### How to allow node libraries like `http`

Solution is to use `--external`.

Without `--external:http --external:https --external:timers` you get these errors:

```
> node_modules/rss-parser/lib/parser.js:2:21: error: Could not resolve "http" (use "--platform=node" when building for node)
    2 │ const http = require('http');
      ╵                      ~~~~~~

  > node_modules/rss-parser/lib/parser.js:3:22: error: Could not resolve "https" (use "--platform=node" when building for node)
    3 │ const https = require('https');
      ╵                       ~~~~~~~

  > node_modules/xml2js/lib/parser.js:17:25: error: Could not resolve "timers" (use "--platform=node" when building for node)
    17 │   setImmediate = require('timers').setImmediate;
       ╵                          ~~~~~~~~
```

#### How to make `real.*` to work

For example, in the html page we do this:

```js
var toggles = new real.QueryStringToggles(document.location.search);
```

To make `real.QueryStringToggles` available, use [`--global-name`](https://esbuild.github.io/api/#global-name).

```
--global-name=real
```

This is like webpack's `library` field.

## Decision

wait for later version.

## Consequences

None really.
