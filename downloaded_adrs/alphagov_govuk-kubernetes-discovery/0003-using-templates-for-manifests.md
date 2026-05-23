# 1. Using templates for manifests

Date: 2017-05-24

## Status

Accepted.

## Context

Kubernetes requires someone to write very verbose manifest files in YAML. Templating
can allow someone to separate the manifest and data and allow a tool to generate
and populate manifest files with ease.

It allows easily understanding the values of a specific application.

It requires us to use a tool on top of plainly writing manifests ourselves.

## Decision

We will not use templates for the time-being, but will re-evaluate our use of
populating common values in the future.

## Consequences

Write everything by hand.

Re-evaluate when we come to working with developers as we should not expect developers
to write everything by hand.
