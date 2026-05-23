# 2. Manage client-side dependencies using Bower

Date: 2016-01-14 (Backfilled 2019-11-10)

## Status

Superceded by [5. Manage dependencies using Yarn](0005-manage-dependencies-using-yarn.md)

## Context

This project was first implemented in plain JavaScript. Its only third-party dependency was on SoundCloud's JavaScript SDK, which was included via a `script` tag.

I had come across package managers while learning AngularJS 1.x. Bower was one of the popular tools of choice at the time.

## Decision

Client-side dependencies will be managed using [Bower](https://bower.io/)

## Consequences

- Client-side dependencies will be installed using Bower thus removing the need to link to hosted versions of the required packages.
- A `package.json` file was added to the project to record its dependency on Bower.
