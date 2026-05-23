# 3. Use AngularJS 1.x

Date: 2016-01-17 (Backfilled 2019-11-10)

## Status

Superceded by [7. Use React](0007-use-react.md)

## Context

This project was first implemented in plain JavaScript. Its only third-party dependency was on SoundCloud's JavaScript SDK.

I had recently discovered frontend web frameworks and had been learning about AngularJS. I was interested in applying it to a larger project.

## Decision

The application will be rewritten in AngularJS 1.x.

## Consequences

- Existing code was pulled into AngularJS constructs such as controllers, directives, templates and services.
- SoundCloud SDK usage was replaced with a service object that made HTTP requests to SoundCloud's web API.
  - In hindsight this may have been unnecessary, or at least I don't recall anything that would have made continued usage of the SDK impossible. 

