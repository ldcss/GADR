# ADR 012: Nested join support

## TL;DR
Expression data is kept in two different Solr indices - analytics and experiment. We need to be able to combine data from both.

## Context
The `analytics` Solr index contains condition data, but as the unstored field `conditionSearch`. We can search on this field, but not display it. To display, we need to include `conditions` from the `baselineCondition` index, using the experiment expression to join the data.

## Decision
The best approach is to add two new searches, for `analytics` and `experiments`. `ExpressionSearch` passes through to an instance of `SolrSearch` 
for searching `analytics` but can join `experiments` to another instance of `SolrSearch`.

This has meant the order of construction and registering of searches in `EndpointSearchProvider` has had to be modified a little.

## Status
Under development

## Consequences
`baselineConditions` has no ID field so cursorMark pagination cannot be used so `SolrSearch` needs to determine if the ID field is present, and if not, use normal, non-cursor pagination.  

Dealing with different names has meant that `SearchType` identity has been overhauled to check the plural and singular names rather than relying on the lower-cased enum name.

## Tags
