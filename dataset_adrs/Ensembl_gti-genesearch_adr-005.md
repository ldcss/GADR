# ADR 005: Search flattening

## TL;DR

We need to support flattening to a specified level e.g. transcripts for a gene search using Elastic. Our chosen approach is to override the ESSearch implementation to include a target for flattening.

## Context

We need to be able to turn this structure:
```
[{name:"ID", description:"Bob", transcripts:[{ID:"t1",start:10},{ID:"t2",start:20}]}]
```
into:
```
[
{ID:"t1", start:10, gene.name:"ID", gene.description:"Bob"},
{ID:"t2", start:20, gene.name:"ID", gene.description:"Bob"}
]
```

The search should also be capable of handling query and output targetted at this level e.g.
```
{"name":"bob", "genes":{"genome":"eric"}} # query
["biotype","id",{"genes":["name","description"]} # output
```

## Decision

Code for this exists in `ResultsRemodeller.flatten` and has to date been invoked by a magic `target` parameters. `Search` has been updated to remove this `target` parameter as part of general changes.

Instead (see adr-004.md) this should be implicit in a given endpoint and concrete search which "knows" to flatten results down. To achieve this, `ESSearchFlatten` has been implemented to use a specified target for flattening in `consumeHits` and `processResults` with minimal duplication of code. All target and flattening code has been removed from `ESSearch`. `ResultsRemodeller.flatten` has been extended with an optional "toplevel" key to support remodelling to promote the targetted fields as "toplevel" e.g.
```{name:"ID", description:"Bob", ID:"t1", start:10, gene.name:"ID", gene.description:"Bob"}```
rather than
```{name:"ID", description:"Bob", transcripts.ID:"t1", transcripts.start:10}```

In addition, ESSearch overrides `query` and `fetch` to transform output and query specification using `transformQueries` and `transformOutput`.

Note that this approach definitely increases complexity, but allows the use of a single repository for genes, transcripts and translations.

## Status
Alpha

## Consequences
Dataset info may need more work to set correctly

Sorting needs adjustment to deal with sorting nested fields for which there is also a filter. This is non-trivial as QueryBuilder is read only.

We may need to consider if a completely flat form is sensible, or if we should aim to use a hash here as this would be more consistent with joining. Needs to be revisited once array representation is investigated properly.

Translations may need more work - the target is translation, but translation is a child of transcript. Could be done with iteration, or a specific instance just for translations. It may be that we don't consider translations at all, and just restrict ourselves to transcripts.

## Tags
ESSearch ESSearchFlatten ResultRemodeller