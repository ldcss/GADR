# 5. Flask architecture

Date: 2017-12-04

## Status

Accepted

## Context

Flask allows you to do whatever you want on your app/folders/templates/etc
and it can quickly become messy.

Plus, to deal with configurations within extensions is harder if you do not
declare the Flask app once and for all then load the configuration.

## Decision

An architecture based on https://github.com/stephane/flask-skeleton

## Consequences

Breaking change, mostly for configurations.
