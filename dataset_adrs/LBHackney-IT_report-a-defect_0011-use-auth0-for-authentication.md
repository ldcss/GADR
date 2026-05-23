# 11. use-auth0-for-authentication

Date: 2019-07-18

## Status

Accepted

## Context

At the moment and for the short term future Hackney do not have a clear candidate for a single sign-on provider. They are reviewing the situation and will decide on a future solution before the end of 2019.

We have so far been using Basic Authentication.

As with other decisions we have attempted to follow the path set by the Repairs Hub which is another Hackney Rails app that is more mature. We asked what they were using and the answer was Microsoft Azure Active Directory using OpenID Connect (OAuth2). We believed we could get the exact same provisioning when the time came for Report a Defect to integrate with a single sign-on provider, however when the time came we learnt that it wasn't supported by Hackney and should be thought of as experimental.

As we had 2 weeks left we discussed with Hackney Architect Keith Gatt the possibility of using Auth0 as a temporary option to enable us to meet the user need of providing agent names within the service, as well as security needs through the use of a logged authentication service that provided one set of credentials per person, rather than a single set for basic auth.

## Decision

Use Auth0 as the single sign-on provider, and remove basic auth from production.

## Consequences

- Auth0 uses Oauth2 standards which makes Report a Defect compatible with any of the mainstream SSO that are currently in contention
- Auth0's pricing strategy puts Report a Defect on their free tier since there will be such few users (5 in the team)
- Auth0 allows other providers to be plugged in such as Google or Microsoft. This means the choice Hackney make can be added to Auth0 and swapped over without requiring Auth0 be completely stripped out
- This will create a second set of user data that is not stored in Hackney's central LDAP system requiring duplicate effort to add new people to and from the New Build Team - dxw's support arrangement will help until it can be swapped to the new SSO choice
- The user experience will not be the same between Hackney's digital services for the NBT - we are not aware of Auth0 being used else where
- Hackney admins can be added to auth0 to take over administration of it if possible and/or required
- Auth0 can be hosted in Europe and we have highlighted and had the risk of storing staff names and emails in another third party service as okay by Keith Gatt
- Auth0 can be set up and managed by the product team which will reduce the potential for blockers which will be valuable as we quickly reach the end of our time here
