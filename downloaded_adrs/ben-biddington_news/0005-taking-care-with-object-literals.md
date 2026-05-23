# 5. Taking care with object literals

Date: 2020-06-12

## Status

Accepted

## Context

Mixing classes and object literals is dangerous because you can have passing tests and an application that does not work.

This test:

```js
it('can be opted-out, and marked deleted instead', async () => {
    const lobsters = new MockLobsters(it => 
        it.listReturns(
            [
                new NewsItem('A', 'item A'),
                new NewsItem('B', 'item B'),
            ]
        )
    );

    const seive = new MockSeive(it => it.alwaysReturn([ 'B' ]));

    const toggles = new MockToggles(it => it.returnTrue('show-deleted'));

    const application = new Application(new Ports(lobsters, console.log, seive), toggles);

    const seivedResult = await application.lobsters.list();

    expect(seivedResult.map(it => ({ id: it.id, deleted: it.deleted }))).to.eql([
        { 
            id: 'A',
            deleted: true
        },
        { 
            id: 'B',
            deleted: false
        },
    ]);
});
```

was written:

```js
it('can be opted-out, and marked deleted instead', async () => {
    const lobsters = new MockLobsters(it => 
        it.listReturns(
            [
                { 
                    id: 'A',
                    title: 'item A'
                },
                { 
                    id: 'B',
                    title: 'item B'
                }
            ]
        )
    );

    const seive = new MockSeive(it => it.alwaysReturn([ 'B' ]));

    const toggles = new MockToggles(it => it.returnTrue('show-deleted'));

    const application = new Application(new Ports(lobsters, console.log, seive), toggles);

    const seivedResult = await application.lobsters.list();

    expect(seivedResult).to.eql([
        { 
            id: 'A',
            title: 'item A',
            deleted: true
        },
        { 
            id: 'B',
            title: 'item B',
            deleted: false
        },
    ]);
});
```

which did pass *because the implementation was written expecting object literals*.

The trouble was, the application did not return those: it works with lists of `NewsItem`.

Nothing failed either, this is the culprit:

```js
// ./src/core/internal/use-cases/news/list.js
module.exports.list = async (list, seive, toggles) => {

    const fullList = await list();
    
    const theIdsToReturn = await seive.apply(fullList);

    if (toggles.get('show-deleted')) {
        return fullList.map(it => {
            it.deleted = false == theIdsToReturn.includes(it.id);
            return it;
        });
    }  else {
        return fullList.filter(it => theIdsToReturn.includes(it.id));
    }
}
```

Specifically:

```
it.deleted = false == theIdsToReturn.includes(it.id);
```

This does not fail when run on a `NewsItem` -- but it also does not produce the expected result, either.

And it's because there's no setter -- adding one produces the correct behaviour.

```
get deleted()      { return this._deleted }
```

```
it.deleted = false
```

does not work without it.

## Decision

The change that we're proposing or have agreed to implement.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
