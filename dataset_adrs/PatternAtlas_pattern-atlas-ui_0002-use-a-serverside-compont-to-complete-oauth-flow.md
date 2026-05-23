# Use a server-side component to complete OAuth-flow

## Context and Problem Statement

To add/modify content on our patternpediacontent repo 'on behalf of the user', we need to use OAuth Authentification in our client-side application. 
But requesting https://github.com/login/oauth/access_token endpoint for creating an OAuth access token does not support CORS ([documented here](https://github.com/isaacs/github/issues/330)). 
Unfortunately, Github prevents you from implementing the OAuth Web Application Flow on a client-side only application (Reason for it: security-related limitations).

## Considered Options

* Use an open reverse proxy like https://cors-anywhere.herokuapp.com/
* Use our own server-side component to complete the flow by using essentially the same logic that [Gatekeepter](https://github.com/prose/gatekeeper) in our uses

## Decision Outcome

Chosen option: "Use our own server-side component", because

* we don't want to provide our their client id and secret to an (possibly untrusted) open reverse proxy (comment from the stackoverflow-article: If the owner of the proxy wants to log credentials from the requests they can)
