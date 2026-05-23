# 1. Use existing APIs instead of creating a project specific API

Date: 2019-04-02

## Status

Accepted

## Context

The Registraties project will need to contain a page that will show data per address (or verblijfsobject) from existing APIs, like [Basisregistraties adressen en gebouwen (BAG)](https://api.data.amsterdam.nl/bag/), [Basisregistratie kadaster (BRK)](https://api.data.amsterdam.nl/brk/) and [Handelsregister (HR)](https://api.data.amsterdam.nl/handelsregister). All required data is readily available.

## Decision

The project's MVP, which will contain a simple search field with auto-suggest functionality, get its data from existing API endpoints and therefore doesn't need its own back-end setup with API. In the future it might, but for the initial phase, the front-end code is capable of retrieving, formatting and showing the data from [api.data.amsterdam.nl](https://api.data.amsterdam.nl).

The application will have container components that have sagas injected into them. Each saga is responsible for retrieving data from a single endpoint. If the situation calls for it, a saga can retrieve data from more than one endpoint.

## Consequences

Not having a project specific API means that, instead of one XHR request per page, multiple requests are needed to retrieve all the data. This will lead to more time needed to completely render a page.

Apart from that, data cannot be shown all at once since some requests depend on the output of other API responses. The page that will show all the data will be gradually filled, section by section. Interface elements, like the table of contents or summary, can 'jump' because of that behaviour.

If, at a later point in time, the decision is made to consolidate the data retrieval, the application needs to be rebuilt so that there is a single saga that retrieves the data instead of having a saga per container component.
