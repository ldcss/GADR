# 8. Objects, function refs and this

Date: 2020-06-18

## Status

Accepted

## Context

If you make a log like this:

```js
class ConsoleLog {
    constructor(opts = {}) {
        this._opts = { allowTrace: false, ...opts };
    };
    
    info(message) {
        console.log(message);
    }

    trace(message) {
        console.log(`ths: ${this}`);
        if (this._opts.allowTrace) {
            console.log(message);
        }
    }
}
```

and then pass a reference to `trace` to another function, `trace` fails because `this` is undefined.

## Decision

The change that we're proposing or have agreed to implement.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
