# 2. Feature Driven Architecture

Date: 2019-08-25

## Status

Accepted

## Context

In previous frontend projects we grouped code by function therefore we had directories "components", "reducers", and "selectors". Introducing updated meant adding changed in a lot of different places of codebase.

We wanted to find a way of stucturing code by meaning. 

The issue motivating this decision, and any context that influences or constrains the decision.

We were influenced by this talks and ideas:

* [How We React at Microsoft - Alex Migutsky](https://youtu.be/CWxc3AYja1I)
* [Ducks Proposal](https://github.com/erikras/ducks-modular-redux)
* [Feature Driven Architecture - Oleg Isonen](https://youtu.be/BWAeYuWFHhs)

## Decision

We decided to try using Feature Driven Architecture.

We split each page into set of semi-independent feature blocks (like "alerts" and "navigationBox"). We create directories for each feature and these directories contain all logic related to this feature (components, reducers, selectors, sagas etc.). We try to move as much logic to features as possible.

Folder structure looks like this:

* src/
  * pages/
    * [pageName]/
  * features/
    * [featureName]/
  * shared/
  * [application scope code]

#### Dependencies

Each feature depend access only the code inside this feature or code in "shared" directory.

Application code is used to compose features together.

If we have dependencies between features, we use application code to take something from first feature and to pass it to second feature. This way every feature has clear composable interface.

We have an index.ts file in each feature directory where we reexport everything we want to be visible from outside. Application code can import things only from index file and cannot import anything else from insife feature. Exception: application can import types from types file since they cannot be reexported.

## Consequences

* Code changes are usually closer to each other now.
* We have clearly defined interface between every feature and the rest of application.
* Sometimes it's hard to define where to place the code.
* Sometimes it's hard to pass configuration from application to features.
* Feature may depend on application to work properly. For example some features need to make api calls but the code for making http calls should be in application scope.
* We managed to enforce import restrictions with unit test.
* It is now theoretically possible to export some features into reusable libraries.
* Although reducers and components are easy composable, we had some difficulties with composing selectors. Even although each selector should only work with data owned by feature, it receives whole state as input and has to find feature state in it. To solve this we let features to tell application where they should be positioned in store but it's a solution to be improved.
