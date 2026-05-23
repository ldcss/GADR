# Auth Strategy: Passport vs. OpenID Connect

- Status: Approved
- Deciders:
  - Kelsie Caldwell @ionab
  - Stephen Fraser @stephenwf
  - Daniel Grant @danielgrant
  - Alan Russell @ajrussellaudio
- Date: 2021-01-14

Technical Story: https://digirati.atlassian.net/browse/WS-110

## Context and Problem Statement

The Identity client app is served from a lightweight Node.js server, which handles OAuth authentication among other things. It achieves this with the Passport auth middleware, and the Auth0 strategy to interact with our auth service.

Auth0 [recently launched](https://auth0.com/blog/auth0-s-express-openid-connect-sdk/) a new SDK for OpenID Connect, an alternative to Passport. In the launch announcement, they stated that development on their own Passport strategy was being reduced to security patches:

> ### What’s Going to Happen to Passport-Auth0?
>
> The answer is… nothing. Unless someone finds a security bug, that is. Passport-Auth0 is used and loved by many Auth0 customers — and remains fully supported. There’s no need to rush updates to your existing apps. We will keep fixing bugs and patch them. We plan to stop adding new features to Passport-Auth0, and the bar for the bugs we fix will be tuned accordingly. If you are about to start a new project, we recommend considering using express-openid-connect, as it will be our target for all innovation for web sign-in on the Node.js platform for the foreseeable future.

## Considered Options

- Continue using Passport
- Drop Passport in favour of OpenID Connect with the Auth0 SDK

### In favour of Passport

- The work to implement user authentication in this project is more or less done already, and meets the customer's requirements.
- The app has no dependency on Auth0's Passport strategy for which development is stopping. Passport integration is achieved with [koa-passport](https://github.com/rkusa/koa-passport).
- The Node.js server uses the Koa framework, but the OpenID Connect SDK is written for Express. Express middleware is not directly compatible with Koa, although solutions to achieve compatibility do exist.
- Passport is used to enable local development. The work that has been already done here would need looked at again, or could be lost altogether.

### In favour of OpenID Connect SDK

- Based on their [examples](https://github.com/auth0/express-openid-connect/blob/master/EXAMPLES.md), Auth0's OpenID Connect SDK seems to _vastly_ reduce the amount of code necessary to achieve the standard aims of user authentication.
- The koa-passport repo has not been updated since July 2019, and the package not published since April 2019. As it is a wrapper around the main Passport library, it is not clear if there are security implications of such a long time without updates. If needed, the Passport dependency can be upgraded independently.

## Decision Outcome

Following discussion, it is decided that the project will continue to use Passport and no work to integrate the OpenID Connect SDK is currently required.
