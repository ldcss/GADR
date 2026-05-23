# Create-react-app as template

## Date

Early 2019 (written on 29 aug '19)

## Status

Accepted

## Context

Using a boilerplate when starting a new project saves you a lot of time writing boilerplate code.

## Decision

At Datapunt we use our own [React Boilerplate](https://github.com/Amsterdam/react-boilerplate-amsterdam) as template. However, this project is based on [Create-React-App](https://github.com/facebook/create-react-app). At the time of creating, there was not yet a department-wide decision on which boilerplate to use. At the time Create-React-App was a valid choice.

## Consequences

This project is not based on the now standard boilerplate. So by default we miss the components and modules that come with our own boilerplate like, Amsterdam-Component-Library, Redux, Sage, Keycloak, etc. On the other hand, Create-React-App has a very large community and there is a lot of help, tips, example code available online.
