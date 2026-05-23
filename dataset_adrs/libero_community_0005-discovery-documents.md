# 5. Use Discovery Documents for requirements and technical choices

Date: 2019-10-11

## Status

Accepted

## [Context](https://github.com/libero/community/issues/23)

Libero product features and architectural choices benefit from the standardization of *discovery documents* that enable collaboration by being shared between team members, across teams, and outside of eLife.

## Decisions

- Always track discovery work in at least one dedicated Github issue.
- If using Google Docs prefix documents titles with `Discovery document:`
- If using Google Docs move them into the single [`Libero` shared drive](https://drive.google.com/drive/u/1/folders/0AC6f8fXdeXmMUk9PVA).
- Link them from the relevant Github issue.
- Establish a timebox in calendar time at the start of the discovery activity.
- Capture questions and answers, and document any assumptions that have been made.
- Link to a [Github milestone](https://github.com/libero/publisher/milestone/20) if applicable.
- Add a `TL;DR` section at the top before closing the document at the end of the timebox.

## Consequences

A timebox helps limiting analysis time to favor prototyping and actual implementation.

Replenishment meetings are a possibility for choosing the length of the timeboxes.

Timeboxes are measured in calendar time so they need to take into account the percentage of time that is allocated to other tasks from the people that work on the discovery.

Github milestones may not exist if the discovery is related to an aspect of the product or to architecture rather than to a particular feature.

There is no explicit way to track the closure of a document on the document itself.
