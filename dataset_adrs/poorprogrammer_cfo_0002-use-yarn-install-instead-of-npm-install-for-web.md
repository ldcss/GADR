# 2. Use yarn install instead of npm install for web

Date: 2020-09-07

## Status

Accepted

## Context

I see found both `yarn.lock` and `package-lock.json` in the repository.

## Decision

Sticking to `yarn` for `web` for now.

## Consequences

Avoid mixing `yarn` and `npm install` which can cause weird errors. 
