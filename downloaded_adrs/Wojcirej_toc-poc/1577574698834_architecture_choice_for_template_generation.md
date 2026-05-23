# Architecture choice for template generation
## Added at: 2019-12-28 23:11:38 UTC
## Status: Accepted

## Context
The POC assumes generation of the table of contents based on the content presented on the page. Data need to be fetched from somewhere, and then presented on the view in some way. Data model won't be simple data structure, as it can be multi-leveled list, which might also contain some behavior, to make it easier to prepare for rendering. It's not going to be simple CRUD application, even if model will not contain much behavior.

## Decision
Use ports and adapters architecture style.

## Consequences
### Positive
* High testability, both unit and integration.
* High configurability.
* Clear separation of concerns between domain and application.
* Enough flexibility to not use all building blocks from DDD in case it's not necessary.
### Negative
* Ports and adapters are usually used for domain models with rich behavior. There is a risk of overcomplication even for the simple application like this POC.

## Other options
* Standard CRUD - even if I won't have much behavior in my models, I don't consider it as a good choice, since I won't have data mapped with view model one to one. I'm also risking to decrease possibility for unit testing.
* Pipes and filters - great for functional programming, with language like javascript, however I don't feel comfortable with modeling in this style yet, hence I could make this development longer and much more complicated for no reason.
