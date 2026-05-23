# 6. collapse to one cloudformation template

Date: 2018-07-14

## Status

Accepted

Supercedes [3. cloudfront distribution means there is long lived infrastruture](0003-cloudfront-distribution-means-there-is-long-lived-infrastruture.md)

## Context

Previously it was decided to have two cloudformation templates. One of which would hold "long lived infrastructure". This was because adding a cloudfront distribution takes a long time.

In practice it isn't possible to only have the cloudfront distribution in the file so the distinction between the two files becomes unclear. And the second template needed some information from the first.

## Decision

To collapse to one template.

## Consequences

The template is getting long so extra care will need to be taken when editing and reading it
