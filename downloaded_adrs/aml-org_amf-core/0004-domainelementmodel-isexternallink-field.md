# 4. DomainElementModel.IsExternalLink field

Date: 2021-01-04

## Status

Accepted

## Context

Linking nodes between different graphs is a feature not provided by AMF/AML. This feature is required by some adopters to:
* Link nodes from a parsed API specification graph with nodes from a parsed dialect instance graph (RestSDK)
* Link nodes between different parsed dialect instances (ANG)

## Decision

Add a boolean field to DomainElementModel called IsExternalLink that marks that a domain element is a reference to a domain element defined in another graph.

## Consequences

This feature was ONLY incorporated to the AML specification
* It is not yet officially supported for API specifications
* It had to be combined with existing AML features for parsing links

Risks
* Adding links to AML dialect instances implies cyclic references can be generated
* This feature is not officially supported for API specifications. However, it is exposed in the in-memory interface and this can lead to miss usages