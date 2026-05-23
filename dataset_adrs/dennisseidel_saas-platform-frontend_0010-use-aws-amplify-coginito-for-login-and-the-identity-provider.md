# 10. Use aws amplify and coginito for login and the Identity Provider

Date: 2019-03-02

## Status

Accepted

## Context

A user expect that he can create an account and login into our application. This should be standard compliant, economical (cheap) and easy to implement.

## Decision

We use AWS Amplify (as a frontend lib) and AWS Cognito as the Identity Provider.

## Consequences

This makes it easy to setup within minuites in the app with the react pre defined components, as well as an mostly standard compliant IDP with AWS Amplify that has a ok pricing model - that is better then Auth0. I have have to check if the application gets more users if it is not more economic to switch to a self hosted version like Keyloak.