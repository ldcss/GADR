# 5/ Use Handlebars as default templating solution
**Author(s)**: Paul Mitchell   
**Status**: Accepted   
**Date**: 13th September 2017

## Context
Prototypes built using the NHSUK prototype kit are a combination of markup and logic that
exhibit a standardised visual language. In order to provide developers easy access to the
visual language and to build dynamic, data-driven prototypes, a templating system that
supports partials and conditional rendering is required. As the intention is to encode
prototype logic in Javascript, the templating system is not required to provide logic
functions of its own.

## Decision
We will provide the [Handlebars](http://handlebarsjs.com) templating system as the default
for the NHSUK prototype kit. A library of Handlebars partials will be provided that encode
the markup necessary for prototypes to use the standard visual language.

## Consequences
  * Developers will need to learn Handlebars in order to build prototypes. Handlebars is
    based on the popular and widely-supported [Mustache](http://mustache.github.io/mustache.5.html) specification
    so it is reasonable to expect developers to be familiar with it already or to be able to learn
    it quickly. The kit will have a set of example prototypes for developers to examine.
  * As the templating system provides no logic functions, developers must encode all the
    logic for their prototypes in Javascript.
  * Developers who need a more functional templating system than the default can install
    one alongside the default.
