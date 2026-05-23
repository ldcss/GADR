# 2. Switch from client side API requests to server side

Date: 2021-02-03

## Status

Proposed

## Context

When designing this application, we decided to make all requests from the client side (using the `useEffect` hook) and we created a proxy middleware which authenticated the API requests and added the API tokens before forwarding the request to the Evidence API.

This allowed us to move quickly, but it had two significant impacts:

1. a UX impact of showing a lot of _"loading"_ messages while client side requests were made
2. an architectural impact of not allowing us to make tamper proof API requests.

An example of point 2:
One endpoint of our API requires a filter parameter of a "service" (roughly linked to a google group). It's important that users are not able to filter by services they are not members of.
We can extract the users' services from their google token, but with the proxy middleware we were not able to attach these filter parameters on the server side, and therefore could allow a user to request any service from their browser.

## Decision

In order to prevent the above impacts, we can remove the proxy middleware and make as many API requests as possible from the server side, and take advantage of Next.js' `getServerSideProps` to pass the fetched data to the component.

## Consequences

This change will detach our client-side and server-side logic, meaning we can make tamper proof API requests from the server. It has the added benefit of improving out user experience by removing the loading messages.

It means a slightly increased workload when creating new interactions with the API, as we will have to implement the serverside component as well as the client side one, rather than relying on the proxy to transparently forward our requests.
