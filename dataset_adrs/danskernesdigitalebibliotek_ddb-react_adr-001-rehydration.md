# Architecture Decision Record: Rehydration

## Context

We are not able to persist and execute a users intentions across page loads.
This is expressed through a number of issues. The main agitator is maintaining
intent whenever a user tries to do anything that requires them to be
authenticated. In these situations they get redirected off the page and after a
successful login they get redirected back to the origin page but without the
intended action fulfilled.

One example is the `AddToChecklist` functionality. Whenever a user wants to add
a material to their checklist they click the "Tilføj til huskelist" button next
to [the material presentation](https://genbib.dk/ting/object/870970-basis%3A54871910).
They then get redirected to [Adgangsplatformen](https://login.bib.dk/login).
After a successful login they get redirected back to the material page but the
material has not been added to their checklist.

## Decision

After an intent has been stated we want the intention to be executed even though
a page reload comes in the way.

We move to implementing what we define as an explicit intention before the
actual action is tried for executing.

1. User clicks the button.
2. Intent state is generated and committed.
3. Implementation checks if the intended action meets all the requirements. In
   this case, being logged in and having the necessary payload.
4. If the intention meets all requirements we then fire the addToChecklist
   action.
5. Material is added to the users checklist.

The difference between the two might seem superfluous but the important
distinction to make is that with our current implementation we are not able to
serialize and persist the actions as the application state across page loads. By
defining intent explicitly we are able to serialize it and persist it between
page loads.

This resolves in the implementation being able to rehydrate the persisted state,
look at the persisted intentions and have the individual application
implementations decide what to do with the intention.

A mock implementation of the case by case business logic looks as follows.

```jsx
const initialStore = {
  authenticated: false,
  intent: {
    status: '',
    payload: {}
  }
}

const fulfillAction = store.authenticated && 
    (store.intent.status === 'pending' || store.intent.status === 'tried')
const getRequirements = !store.authenticated && store.intent.status === 'pending'
const abandonIntention = !store.authenticated && store.intent.status === 'tried'

function AddToChecklist ({ materialId, store }) {
  useEffect(() => {
    if (fulfillAction) {
      // We fire the actual functionality required to add a material to the 
      // checklist and we remove the intention as a result of it being
      // fulfilled.
      addToChecklistAction(store, materialId)
    } else if (getRequirements) {
      // Before we redirect we set the status to be "tried".
      redirectToLogin(store)
    } else if (abandonIntention) {
      // We abandon the intent so that we won't have an infinite loop of retries
      // at every page load.
      abandonAddToChecklistIntention(store)
    }
  }, [materialId, store.intent.status])
  return (
    <button
      onClick={() => {
        // We do not fire the actual logic that is required to add a material to
        // the checklist. Instead we add the intention of said action to the
        // store. This is when we would set the status of the intent to pending
        // and provide the payload.
        addToChecklistIntention(store, materialId)
      }}
    >
      Tilføj til huskeliste
    </button>
  )
}
```

We utilize session storage to persist the state on the client due to it's short
lived nature and porous features.

We choose Redux as the framework to implemenent this. Redux is a blessed choice
in this instance. It has widespread use, an approachable design and is
well-documented. The best way to go about a current Redux implementation as of
now is [`@reduxjs/toolkit`](https://redux-toolkit.js.org/). Redux is a
sufficiently advanced framework to support other uses of application state and
even co-locating shared state between applications.

For our persistence concerns we want to use the most commonly used tool for
that, [`redux-persist`](https://github.com/rt2zz/redux-persist). There are some
[implementation details](https://redux-toolkit.js.org/usage/usage-guide#use-with-redux-persist)
to take into consideration when integrating the two.

## Alternatives considered

### Persistence in URL

We could persist the intentions in the URL that is delivered back to the client
after a page reload. This would still imply some of the architectural decisions
described in Decision in regards to having an "intent" state, but some of the
different status flags etc. would not be needed since state is virtually shared
across page loads in the url. However this simpler solution cannot handle more
complex situations than what can be described in the URL feasibly.

### useContext

React offers [`useContext()`](https://reactjs.org/docs/hooks-reference.html#usecontext)
for state management as an alternative to Redux.

We prefer Redux as it provides a more complete environment when working with
state management. There is already a community of established practices and
libraries which integrate with Redux. One example of this is our need to persist
actions. When using Redux we can handle this with `redux-persist`. With
`useContext()` we would have to roll our own implementation.

Some of the disadvantages of using Redux e.g. the amount of required boilerplate
code are addressed by using `@reduxjs/toolkit`.

## Status

Accepted

## Consequences

- We are able to support most if not all of our rehydration cases and therefore
  pick up user flow from where we left it.
- Heavy degree of complexity is added to tasks that requires an intention
  instead of a simple action.
- Saving the immediate state to the session storage makes for yet another place
  to "clear cache".
