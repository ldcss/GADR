# 7. Svelte and events

Date: 2020-06-15

## Status

Accepted

## Context

Svelte does support our existing events:

```html
<script>
    application.on('rnz-news-item-deleted', e => { 
        console.log(e);
    });
</script>
```

The tricky part is going to be editing the list to remove the item.

In the interim we can use the identical handlers to vanilla as it just works:

```js
application.on('rnz-news-item-deleted', e => {
    const list = document.querySelector(`div#rnzNews .items`);

    const elementId = `news-${e.id}`;

    const selector = `div#rnzNews li#${elementId}`;

    const listItem = document.querySelector(selector);
    
    try {
        list.removeChild(listItem);

        console.log(`Item deleted <${e.id}>`);
    } catch (error) {
        console.error(
            `Failed to delete <${e.id}> with selector <${selector}>` + 
            `The error is: ${error}`);
    }
});
```

We could deduplicate these I guess.

## Decision

Look at [bindings](https://svelte.dev/docs#bind_group) perhaps as a better way of adding list items. We have 

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
