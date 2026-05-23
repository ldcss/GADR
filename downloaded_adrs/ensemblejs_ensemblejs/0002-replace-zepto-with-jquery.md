# 2. Replace Zepto with jQuery

Date: 19/05/2016

## Status

Accepted

## Context

The current approach for templates uses pug (jade) templates that are browserified into the client during the build step. These are appendend to the document. The issue with this approach is that `script` tags are not executed.

jQuery has an method called `getScript` that will get a script and in the success callback we can run more javascript. The zepto port of jQuery does not support this method.

## Decision

Replace all instances of zepto with jQuery.

## Consequences

Zepto is meant to be faster than jQuery. However, zepto has not been updated in six months and has received somewhat sporadic updates. jQuery is kept up to date and anecdotally performs better than it used to.
