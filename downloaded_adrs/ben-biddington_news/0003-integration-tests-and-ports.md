# 3. Integration tests and ports

Date: 2020-06-06

## Status

Accepted

## Context

There are two ways I can currently see of doing this, one is building stubs into bundles, the other is serialization of port functions
in the test:

```js
async supplyPorts(ports = {}) {
    this._page = await this.page();

    await this._page.evaluate(fun => {
      core.queryWith(() => eval(fun)());

      core.onSaved(e => console.log(`[ACTION.SAVED]`));
      
      window.console.log(`Reset hacker news port and added action listener`);

      core.news();
    }, ports.top.toString());
  }
```

Note the `ports.top.toString()`, this is serializing a function. 

This still leaves us disconnected, though -- we can't then use it as a mock because it does not share memory with the test.

The function has been serialized and sent across the wire.

## Decision

The change that we're proposing or have agreed to implement.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
