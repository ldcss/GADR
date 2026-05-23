# 11. On application state

Date: 2021-03-30

## Status

Accepted

## Context

We have come across a case where we can see the difference between application state and UI state.

The application use the `show-deleted` to determine whether or not it filters out deleted (seen) articles.

We would like to be able to change the display based on this toggle.

1. Change a toggle switch in the UI
1. Update the toggle in application
1. Have the UI update in response

As it stands now you have to reload thr screen, supplying the toggle as query string param.

We do not have a mechanism for binding to application itself.

At the moment all view implementations use their own state and property represenations.

We need a way of binding to application state.

This means either:

1. Copying state updates to web layer
1. Modifying application to expose state fields and let control bind directly 

This concept is similar to what functions like `mapStateToProps` are for: automatically handling the transfer of state changes from a redux store to react component. 

Q. Why is it mapping to props though and not to state?.

<details>
  <summary>The 'show-deleted' toggle</summary>

  The `list` use case behaves differently depending on its supplied `toggles` argument:

  ```js
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

  That argument is state stored internally by `Application` as `_toggles`. The idea is that the toggles are supplied at startup and used thereafter.

</details>

### UI representation

Normally when databinding a UI library, this kind of toggle is present as some kind of **reactive state**.

```js
// svelte
$: uiOptions = {
  showDeleted: toggles.get('show-deleted'),
}
```

```js
// ficus.js
state() {
  return { 
    lobstersNews: [],
    hackerNews: [],
    uiOptions: {}
  }
}
```

It seems as though each library is set up with its own methods for this because *that* is how they minimise rendering.

They all seem to be bound to some kind of data structure: `this.state` or svelte's reactive fields.

In order to enable automatic binding, changes *must* be broadcast through this mechanism. 

The rest of the framework does rendering based on changes to these state representations, taking care of when and what to render.

### Disconnect

In this case of the `show-deleted` toggle, we need to be able to both maintaina the application as the source of truth 
**--and--** allow reactive state binding.

How you do that: 

* without lots of work?
* without limiting to a single methodology, i.e., tying to specific store?

## Decision

The change that we're proposing or have agreed to implement.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
