# Routing

## Context

* We are building a web app that has one official url that uses query params
* The url is /search?q=search-term
* We believe that future endpoints will be added, or more complicated search requests

## Decision

* We will use Bidi to parse the routes.

## Alternatives considered

* Given the simplicity of the URL structure, we could get away with not using any routing.
* Compojure is an option, however we feel that it's reliance on Macro's could harm future development.

