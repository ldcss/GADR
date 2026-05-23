# 2. Use chrome.identity.launchWebAuthFlow instead of chrome.identity.getAuthToken

Date: 2017-07-14

## Status

Accepted

## Context

A method to authorize against the youtube API to get the access token needs to be added to the application.

## Decision

I decided to use the launchWebAuthFlow instead of the getAuthToken api to do the oauth2 authentication. This is
because getAuthToken can only authorize the google signed in in chrome. This prevents me from using a different account
for youtube from my chrome account.

## Consequences

Chrome can't manage the access token and automatically update and revalidate in the background.
