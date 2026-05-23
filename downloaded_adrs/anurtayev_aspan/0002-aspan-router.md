# 2. Aspan Router

Date: 2020-04-26

## Status

Accepted

## Context

Routing is required for Apspan Client applicatoin. I am not using a location bar to navigate between pages. Threfore React Router is not an option.

## Decision

I will implement custom router with GraphQL based state.

Router will control type of the main screen component based on state variables.

Application starts with a Folder component showing root folder content. Possible successors - Image and MetaData. From Image user can go further to MetaData or back to Folder containing that image.

Transition from Folder to Image:
{
screen: Folder
id: ID
}
{
screen: Folder
id: ID
}

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
