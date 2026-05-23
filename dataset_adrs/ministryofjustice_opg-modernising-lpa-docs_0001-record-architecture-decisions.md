---
layout: layouts/adr.njk
title: "Record architecture decisions"
weight: 1
date: 2021-06-27
review_in: 12 months
tags: 
    - adr
    - open_source
    - open_data
areas_of_coverage: ["Digital Service"]
status: "accepted"
contributors: ["John Nolan"]
adr_number: "0001"
---

## Context

We need to record the architectural decisions made on this project.

## Technical

### Interoperability - How does this enable the exchange of information

Allows anyone to be able to follow and contribute to ongoing decisions made on the service.

### Developer Knowledge - How well known is this in our current skill sets

**Overall**: 8/10
Developers are aware of ADRs, but their experience of doing them brings this score down a little.

### Support/Open Source - Is it well supported

Fully Open Source.

### Scalability

Uses Markdown and git to achieve scalability.

## Ethics

### Mitigate against being tech deterministic

Giving visibility to our decisions and allowing contributions ensures Citizens and colleagues are able to have a voice and be aware of changes over time.

### Ensure you conduct inclusive research

The design of the pages ensures the site is accessible to the highest standard. This is achieved by using the GDS pattern library.

In the future we should look at including a Welsh version to be more inclusive.

Language within the ADRs will contain technical language so may not be accessible to persons not familiar with the terminology.

### Think big and imagine what the impact of your work can be

Decisions can be read and commented on inside and outside of government. Encouraging conversation with others exploring these technologies will enable better communities and feed back into our own decisions.

This will allow us to get a wider range of opinions on our decisions which we could not have got before.

### Interrogate your data decisions

N/A

### Decision

We will use Architecture Decision Records, as [described by Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions).

### Consequences

See Michael Nygard's article, linked above.

ADRs will be public for visibility and collaboration.

Pull requests and Github issues can be used to drive conversations.
