# 9. On testing with events

Date: 2020-06-23

## Status

Accepted

## Context

We have had some flaky tests that are due to timing of events.

Because the initial render is non-deterministic, firing test events may give the wrong results.

```js
// test/integration/web/ui/bookmarks-examples.js
describe("list items are added in response to 'bookmark-added' notification", () => {
    let interactor, page, consoleMessages = null;
    const itemsSelector = 'div#application div#bookmarks .items';

    before(async ()  => 
    {
        interactor      = new WebInteractor({ headless: true });
        page            = await interactor.page();
        consoleMessages = new ConsoleListener(page);
    });

    beforeEach(async () => {
        await page.goto(`${baseUrl}?unplug=1&${feature}`, { waitUntil: 'domcontentloaded' });
    });
        
    after(async () => await interactor.close());

    it('for example', async () => {
        await page.once('load', async () => {
            await page.evaluate(() => {
                application.notify(
                    'bookmark-added',
                    { id: 'id-1337', title: 'Title 1', url: 'http://abc/def', source: '' }
                );
            });
        });
        
        await page.waitForSelector(`${itemsSelector} li`);

        const listIds = await page.$$eval(`${itemsSelector} li`, items => items.map(it => ( it.id )));

        expect(listIds).to.eql([ 'bookmark-id-1337' ]);
    });
});
```

Here if the `bookmark-added` notification is sent before the page has loaded, then the test will fail because 
`div#application div#bookmarks .items` would have been overwritten.

## Decision

Now trying introducing the idea that there is something in the html page called `view` that monitors load events:

```js
class UIEvents {
    constructor(opts = { }) {
        opts = { idlePeriod: 200, ...opts }
        this._idlePeriod = opts.idlePeriod;
        this._lastRender = this.now();
    }

    notifyRendering() {
        this._lastRender = this.now();
    }

    async waitUntilIdle(opts = { }) {
        opts = { timeout: 500, ...opts };

        const startTime = new Date();
        
        const timedOut = () => new Date() - startTime >= opts.timeout;

        const delay = ms => new Promise(res => setTimeout(res, ms));

        while(false == this.isIdle()) {
            if (timedOut())
                throw new Error(`Timed out after <${opts.timeout}ms>`);

            await delay(10);
        }
    }

    isIdle() {
        return (this.now() - this._lastRender) > this._idlePeriod; 
    }

    now() { return new Date(); }
}

module.exports = { UIEvents }
```

This *does* require views to add notifications like:

```js
import { afterUpdate } from 'svelte';

afterUpdate(() => {
    window.view.notifyRendering();
});
```

@todo: I guess we should add tests for that: make sure each view type raise these.

### Attempt 1

Tried using [`page.once`](https://github.com/puppeteer/puppeteer/blob/main/src/common/Page.ts), which is supposed to be a callback for pad load.

It did work for a start but only by fluke I think.

### Decided against

* forcing views to implement a finished notification
* changing `Application` to notify when finished

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
