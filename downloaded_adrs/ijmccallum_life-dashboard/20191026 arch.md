# How will this thing be architected?

High level overview of the structure of the thing.

## Context

Need to decide on a high level structure for this app to take. It's goals are:
 - Me to learn
 - Fun times / be aspirational (as a selling point if it ever gets published seriously)
 - be a potential thing I'll publish
 - make some elements of life easier / be an enabler to life automation.

## Choices - pros cons

- **Federated syncing**. Multiple devices, standalone instances of the app. They sync whenever they can. Will need conflict resolution. Could avoid internet security by optionally only allowing direct connections.
  - Pros:
    - an excuse to use git under the hood for conflict resolution possibly. A way of introducing branches to the public? Or at least conflict resolution
    - more resiliant
    - A way of creating your own internet? This is kind of exciting!
  - Cons:
    - Each device type would need native coding, probably: desktop & mobile native. (could spin as a positive, loads of learning)
    - Complexity! Would be a decent challenge.
- **Federated Locking**. Same as syncing but without the syncing. You can only edit data on one device, in order to change the master all instances need to be connected. NOPE too restrictive, not aspirational.
- **Phone as primary**. Think WhatsApp: the app on your phone would be the primary. You can only run the app in other places if there is an active connection to the phone.
  - Pros:
    - Excuse to play with real time connections.
    - Single source of truth - no conflicts to deal with!
    - your phone is pretty much always connected to the internet.
  - Cons:
    - Restricts the use of the app to your phone only, although your phone is usually the hub of all things
    - What language to use, probably not python :(
- **Desktop as primary**
- ****
- **Hosted server** A true online service
  - Pros
    - I already know this
  - Cons
    - Server maintenance
    - Privacy issues / this is the centralized nightmare we're building ourselves into

## Decision

"Federated syncing". It's aspirational, one hell of a challenge, awesome for the CV. The main con for this is complexity... but this _is_ a learning project so: bring it on! Next up is to sketch out the layout of the pieces.