# 9. Develop admin tool as SPA

Date: 2021-01-11

## Status

Accepted

## Context

As part of the functional requirements, we need to have a means of managing the content through an intuitive web 
interface. There are a couple of options to achieve this

### 1. As a "traditional" web application in the MVC architectural style, embedded within the backend (monolith)
#### Pros

- Server-side rendering sometimes can provide better user experience since content is immediately visible once 
the page is loaded
- Compatibility issues between the frontend and backend can be detected at the earlier stage

#### Cons

- Tools and libraries for the backend and frontend are mixed in the same project, making it a bit messy and mentally harder to grasp
- Strong coupling between web layer and backend discourages us to design general-purpose API for other types of potential consumers
- Provides limited level of interactivity

### 2. As a Single Page Application in the MVVM architectural style, packaged and deployed separately from the backend
#### Pros

- Frontend is more decoupled from backend technologies since they interact with each other via API
- Backend API can be potentially used by other consumers too: CLI, Native & Mobile (as long as it is general-purpose)
- Frontend and backend can be delivered independently (and hence faster) from each other
- Provides greater level of interactivity

#### Cons

- More pipelines need to be maintained in CI
- Compatibility issues between the frontend and backend may be detected later, during the integration stage
- Complete client-side rendering may degrade the user experience a bit

## Decision

We will go for the SPA approach

## Consequences

- Initial development pace might be slower, since we will have to learn the new frontend technologies as we go
- We will explore modern frontend technologies and approaches
