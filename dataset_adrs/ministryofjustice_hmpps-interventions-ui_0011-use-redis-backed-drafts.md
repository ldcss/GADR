# 11. Use Redis-backed drafts

Date: 2021-06-28

## Status

Accepted

## Context

### Background

Our service frequently needs to take a user through a journey which involves asking them a series of questions over multiple pages, and then playing all the answers back to the user before finally submitting all the answers to the interventions service API.

This means that we need somewhere to store the user’s answers as they progress through the journey. For some journeys, the interventions service provides this storage. For example, in the journey of submitting a referral, the interventions service provides endpoints for creating and updating a draft referral.

However, we have other journeys where the interventions service does not provide this storage. For example, assigning a referral to a caseworker, or cancelling a referral. For these journeys, the UI application needs to provide its own storage.

### Why not have the interventions service store everything?

We _could_ make the interventions service provide storage for the data of every page of every journey in the UI. However, this would be very tied to the user journeys of this UI and less of a general-purpose interventions API. We should reserve interventions service storage for long journeys which the user might want to complete in multiple sittings.

### The solution so far

We pass data from page A to page B to page C of a journey by making sure that the HTTP request for page C includes all of the data that was submitted on pages A and B. We do this either by:

- accepting the data from previous pages as data encoded in the request URL’s query, and then passing it in a GET request to subsequent pages by placing the data from previous pages into the query of the URL that’s used for navigating to the next page
- accepting the data from previous pages as `application/x-www-form-urlencoded` form data, and then passing it in a POST request to subsequent pages by placing `<input type="hidden">` fields on each page, replaying the data from the previous pages

### The problem with this solution

Using a GET request limits the amount of data a user can submit on a page, since many clients and servers do not support URLs over 2000 bytes long.

Using a POST request means that we cannot redirect to different pages in the journey (for example, check your answers) based on the user’s input, since a redirect response cannot instruct the browser to make a POST request.

Also, the approach of embedding the data in the HTML is laborious. We have to make sure that every possible route through the pages in the journey preserves the data. This becomes particularly easy to get wrong when we have non-linear sequences of pages — for example, a link on the check your answers page that allows the user to edit a previous answer.

### Other requirements for a solution

The solution must also:

- make sure that a user is not able to access data entered by a different user
- not prevent the user from performing the same journey multiple times concurrently — for example, they should be able to assign two different interventions at the same time in different browser tabs
- preserve the data that the user entered on previous pages when they use the browser’s Back button
- give us maximum flexibility in deciding how to meet [WCAG 2.1’s Success Criterion 2.2.1 Timing Adjustable](https://www.w3.org/TR/WCAG21/#timing-adjustable) — for example, by making sure that the data is kept for at least 20 hours before it expires

It would also be good if the solution could:

- not introduce new dependencies to the service — for example a database
- allow us to continue using the same kinds of coding patterns as we do when interacting with the interventions service API — creating and updating a resource
- allow us to identify and clean up old data

## Decision

We’ll use the UI application’s existing Redis server as our storage. It allows us to store essentially unlimited amounts of data.

In Redis, we’ll store “draft” objects. These are containers of arbitrary JSON data, along with:

- a globally unique identifier
- the unique identifier of the user who created the draft
- timestamps of creation and last update
- an identifier explaining what type of data the draft represents

We’ll:

- provide a “CRUD” API for creating, fetching, updating and deleting these draft objects
- include the draft’s ID in all URLs in a journey
- allow these drafts to be created by a GET request, so that we can use `<a>` tags to link to journeys
- prefer to use POSTs to pass data to a page instead of GET, so we don't have to worry about body size constraints

The aforementioned API will:

- enforce access control — making sure that a user is only allowed to access drafts that they created
- make sure that drafts are automatically removed after they are no longer accessed for a certain amount of time (for example, 1 day), using Redis’s expiry functionality, to make sure that drafts do not consume storage in Redis indefinitely

### Alternatives

We might consider using the (Redis-backed) Express `session` object. However, this object expires after 2 hours of inactivity, which is insufficient for our needs. We don’t want to increase this timeout since there are security implications to increasing the amount of time that a user remains logged in to the service.

## Consequences

Draft data will be lost after a period of inactivity. We should inform the user when this has happened, so that they can start the journey again. If this time limit proves to be a problem then we may need to reconsider the expiry duration.

The URLs for some pages in our service will become longer.

The draft data will only be as secure as our Redis instance.
