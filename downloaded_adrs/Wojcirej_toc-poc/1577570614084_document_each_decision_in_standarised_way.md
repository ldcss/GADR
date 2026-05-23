# Document each decision in standarised way
## Added at: 2019-12-28 22:03:34 UTC
## Status: Accepted

## Context
Usually development comes at full pace as soon as there is some work to do.
During development, plenty of decisions are being made.
Some of them are even made before development itself, based on drivers.
This is only proof of concept, but at the same time, even in development of POC some decisions are made.
When I come back to it on some day, I want to know why I made this and not other decision.

## Decision
Document each decision with ADR (Architecture Decision Record). Each decision will constitute a markdown document with title, date of decision, its status, context providing background and preconditions for the decision, and listed positive/negative consequences. Filename of each decision will have included timestamp and title in `snake_case` convention. All decision will be store in `doc` directory. They will constitute Architecture Decision Log. Each record will be immutable.

## Consequences
### Positive
* Will have rationale of every single decision I've made.
* Won't need to remember much.
* It will be easier to share the details in case someone will be interested in anything related to the project.
* Increased probability of each decision to be more mature, more well-thought and more aware, without much coincidence.

### Negative
* More effort required in preparation of such ADRs.
* More discipline required in maintenance and documenting such decisions.

## Other options
* Comments in the code - less effort, but dirtier codebase. Will not make the code more readable, and not every decision will be possible to document in this way.
* Documentation generated via string docs or anything like that - potentially better than comments in the code, however not every decision will be possible to document in this way. In addition to this, this only covers one level of the application - the code.
