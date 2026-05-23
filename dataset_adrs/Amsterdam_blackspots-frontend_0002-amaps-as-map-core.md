# Amaps as map core

## Date

Early 2019 (written on 29 aug '19)

## Status

Accepted

## Context

It normally saves time to use boilerplate or generic components available when starting a new project. The most important piece of this application is its map component and the UI a map provides.

## Decision

When starting this project, I ([Bennie van der Wel](https://github.com/BennievanderWel)) had little experience with map application. Datapunt had a generic component, called [amaps](https://github.com/Amsterdam/amaps) which was a generic map component tailored for Amsterdam based on [Leaflet.js](https://leafletjs.com/). We used this a our core for the map component since it had a lot of features we need already build-in. Also, amaps was meant to be used in relatively small application as this one.

## Consequences

Amaps works out of the box with features like street search, gray-scaled map and zoom features. However, amaps comes with quite a large footprint (mainly due to the amsterdam-stijl css). Also, amaps wraps some parts of Leaflet making those parts hard to reach.
