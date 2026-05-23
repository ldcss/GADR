# Using react-hook-form for editing data

## Date

Oktober 2019

## Status

Accepted

## Context

The form input functionality is required. At datapunt there are 2 different form packages used for dcatd_admin (react-jsonschema-form) and signals-frontend (react-reactive-form) but the experience learnd that they are difficult to be used for the requirements that we have.
Therefore there is a new research done and the new package [react-hook-form](https://react-hook-form.com) that was this year released seems to be closer to our project needs of this moment. This package is also suitable to be used with the [Amsterdam Styled Components](https://github.com/Amsterdam/amsterdam-styled-components)

## Decision

For this project the form functionality will be implemented with the react-hook-form package.

## Consequences

Because is a new package a learning curve for good practice usage is expected.
