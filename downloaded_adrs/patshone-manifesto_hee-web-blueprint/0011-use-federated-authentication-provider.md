---
layout: layouts/page.njk
title: ADR-0011 Use federated authentication provider
pageTitle: ADR-0011 Use federated authentication provider
pageDescription: 
path: /blueprint
permalink: /blueprint/adrs/ADR-0011-use-federated-authentication-provider.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0011 Use federated authentication provider
  order: 11
---

# 11. Use federated authentication provider

Date: 2020-04-11

## Status

Pending

## Context

We need to describe an approach to authentication that supports the use of multiple authentication providers. Azure AD provides the ability to configure direct federation with a range of authentication providers and includes the ability to provide managed authorisation for users without the ability to authenticate with Azure AD 

- https://docs.microsoft.com/en-us/azure/active-directory/b2b/delegate-invitations

## Decision

We will choose an authentication provider/platform that supports the federation of authentication.

## Consequences

This means that users, particularly those with OpenAthens user accounts will be able to authenticate with our platform using either their Office 365 credentials, their OpenAthens credentials or other Azure AD native credentials
