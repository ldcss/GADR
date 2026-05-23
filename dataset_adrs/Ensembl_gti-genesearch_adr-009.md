# ADR 009: Solr search

## TL;DR

A Search instance has been provided that supporting querying Solr databases, as required for GXA querying.

## Context

We need to be able to query the GXA (Gene Expression Atlas) data set to attach expression data to genes. The most appropriate interface to this database is a Solr instance available from within HX. 

## Decision
We have implemented the following endpoints:
* `SolrSearch` - a generic Search implementation using `SolrSearchBuilder`. This is not currenty tested completely as there is no easy way to set up an embedded Solr server (EmbeddedSolrServer doesn't work in my hands and appears to be discouraged anyway)
* `ExpressionSearch` - a join/merge implementation using `SolrSearch`
* Expression endpoints (query, fetch, info, object) using `ExpressionSearch`

Solr is a good fit with ES (natch) so relatively few changes exist. Facets and `select` are not currently supported.

## Status
Under development

## Consequences
Facets and `select` are not currently supported.

Testing is not currently supported.

## Tags
Search, SolrSearch, ExpressionSearch
