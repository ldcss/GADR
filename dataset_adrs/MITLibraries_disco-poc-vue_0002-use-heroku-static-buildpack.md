# 2. Use Heroku static buildpack

Date: 2020-09-15

## Status

Accepted

## Context

We need to decide how to deploy our Vue app in Heroku. We can achieve this either 
by using a Node.js web server, or by deploying the app as a static site with 
the [Heroku static buildpack](https://github.com/heroku/heroku-buildpack-static).

## Decision

We will use the static buildpack to deploy, as our app will essentially be a 
static frontend backed by TIMDEX. This is consistent with [Vue's deployment 
guidelines](https://cli.vuejs.org/guide/deployment.html#general-guidelines)
on deployments.

## Consequences

The static buildpack began as a community project. It is now owned by Heroku, but 
they still consider it ["an experimental OSS project"](https://github.com/heroku/heroku-buildpack-static#heroku-buildpack-static). Though the buildpack appears 
to be widely used, our decision to rely on it introduces some risk.

In the event that the buildpack becomes unsupported, we would need to reevaluate 
our options. At present, [Express](http://expressjs.com/) seems to be the most 
popular choice for deploying Vue to Heroku, and the change cost would be 
relatively low.
