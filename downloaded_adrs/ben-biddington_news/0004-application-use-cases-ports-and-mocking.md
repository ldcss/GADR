# 4. Application, use cases, ports and mocking

Date: 2020-06-06

## Status

Accepted

## Context

Skewering the UI requires a different kind of isolation to the rest of the application. 

This is what we have in the integration tests:

```js
const { MockLobsters }       = require('../../../../test/support/mock-lobsters');
const { Application, Ports } = require('../../../core/application');

module.exports.application = () => {
    return new Application(new Ports(new MockLobsters()));
};
```

This is *not* what we want. It has set up the application with its ports stubbed.

We want to isolate the web view part entirely from the applications port requirements.

We want to be able to make this kind of statement:

```
When the UI executes some action it calls this use case
```

We don't want the view to know *anything at all* about the application's dependencies.

It's only when unit testing `Application` that we want to know about `Ports`.

The difficulty is arranging both applications so that they have the same shape. Prior to making the last change, we had both
sets of tests passing but the application was no plugged in correctly. 

## Decision

Keep a separate mock application apart from the real one for a while.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
