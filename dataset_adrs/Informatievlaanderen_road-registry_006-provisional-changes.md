# 6. ETL

Date: 2021-04-01

## Status

Accepted

## Context

As a result of running the feature-compare process a bunch of files are produced. These files are essentially a _diff_ between what the operator started out with, that is the dump / extract he / she started working from, and what they ended up with, after having edited shapes and associated data in their editor. Some of those files have a `_ALL.DBF|_ALL.SHP` suffix. These files are the files we base our logic on to validate and translate to an _internal_ change request. Most notably, these files have an extra column called `RECORDTYPE` which, as the name suggests, classifies a record as either being `IDENTICAL`, `ADDED`, `MODIFIED` or `REMOVED`. Next to that most of the files contain, per record, the equivalent of a primary key that identifies a row. This primary key is used in other files as a foreign key to reference a record sitting in another file. Records with a `RECORDTYPE` of `ADDED` will use a temporary identifier (a really big number that we assume is free to use) to make this work (see [004-temporary-and-permanent-identifiers.md](004-temporary-and-permanent-identifiers.md) for how that works). One gotcha is that the primary keys are not always unique, that is, they can appear multiple times in the `*_ALL.DBF|*_ALL.SHP` files, once for each record type. A common scenario is a modification represented as a removal and an addition record.

For the `WEGSEGMENT_ALL.DBF` file, things are more complicated ... next to having a `WS_OIDN` column act as primary key it has a `EVENTIDN` column acting as an alternative primary key in some cases. In case the `RECORDTYPE` is `ADDED` and the `EVENTIDN` has a value differing from `0`, the `WS_OIDN` column refers to an existing road segment and the `EVENTIDN` column refers to its new representation. In such a case, other files refer to a road segment by the value found in the `EVENTIDN`, not by the value in `WS_OIDN`. Alas, such is life ...

## Decision

Modifying a road segment involves data from `WEGSEGMENT_ALL.DBF`, `WEGSEGMENT_ALL.SHP` and `ATTRIJSTROKEN_ALL.DBF`, `ATTWEGBREEDTE_ALL.DBF`, `ATTWEGVERHARDING_ALL.DBF` - that is, when it is represented as an _internal_ change request command. Each of those `.DBF` files contains a `RECORDTYPE` column. As such, a road segment could be marked as identical in `WEGSEGMENT_ALL.DB`, yet it's lanes, width and / or surfaces could be marked as a mixture of modified, removed, added, identical. This is the reason why a road segment that is identical is appended as a `provisional` change to the list of translated changes. Because we're not sure, just yet, that it is an actual change. The order in which these files are translated causes a `provisional` change, if warranted, to be promoted to an actual change.

Why go thru all this trouble? Well, lanes, widths, and surfaces are tightly coupled to the geometry of a road segment such that it makes sense to capture them as a holistic change rather than as individual fragmented changes. There's still a bigger debate to be had about which pieces of data change together ...

## Consequences

This behavior matches the operator's mental model.
