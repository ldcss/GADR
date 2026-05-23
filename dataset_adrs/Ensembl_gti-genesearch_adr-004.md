# ADR 004: Merge/join architecture

## TL;DR

To support joins between different data stores and different data types, and merging of data from two searches, we need to reconsider the architecture used for carrying this out. We will implement a new base search mechanism which will be instantiated using the appropriate behaviour for each data type.

## Context

We need to be able to specify a target and have that target be the focus
e.g.
genes, with variations mapped to them
variations, with genes mapped to them
transcripts, with genes mapped to them
genes, with transcripts mapped to them
sequences, with genes mapped to them
genes, with sequences mapped to them

Ultimately, we may also need 3-stage joins as well (expression->genes->variations). The current implementation is too restrictive.

## Decision

Rather than overloading a search with complex behaviour, this boils down to needing to have one endpoint per data type
e.g.
/api/genes/query?fields=[name,genome,variations:{id}]
/api/variations/query?fields=[id,genes:{}]

This might use the same search underneath e.g. a transcript-based ESSearch, which automatically does the retargetting and restructures fields and queries accordingly. This allows a merge search to deal with these in batches as required.

A join/merge search would work as follows:
* decompose queries and fields to split them into "from" and "to"
* query the primary db including join field
* hash results (in batches)
* for the hits, query the secondary and then pull back and add to the results

Note that pass-through targets are no longer a consideration - a gene search will contain transcripts as before. Note that we may need to flatten out sub-fields in ESSearch though.

A merge strategy can be specified to deal with situations where the "join object" is already present in the "from" results.

For instance, homologues are merged into the "from" homologues.

A new implementation `JoinMergeSearch` now replaces `JoinAwareSearch`.

## Status
Alpha

## Consequences
Dataset info may need more work to set correctly

Flattening is no longer be something that an endpoint can be told to do - instead, different endpoints will automatically flatten to the desired level.

For instance, to flatten to transcripts, use a `TranscriptSearch` which "knows" that the results have to be flattened to transcript. See adr-005.md for more details.

New search implementations are needed for each data type:
* `GeneSearch`
* `GenomeSearch`
* `TranscriptSearch`
* `TranslationSearch`
* `SequenceSearch`
* `HomologueSearch`
* `VariationSearch`
* `ExpressionSearch`
* etc.

This may be inadequate for some situations where the "from" side is far larger than the "to" side e.g. from variation to gene. In this case, the logic would need to be flipped to query the "to" set first and then restrict the "from" side accordingly.

## Tags
JoinAwareSearch, GeneSearch, JoinMergeSearch
