# 3. Install all base dependencies

Date: 2019-11-01

## Status

Accepted

## Context

It is possible to install any dependencies for child services in this base
image. Doing so increases the image size, but speeds up child image builds.

## Decision

We will install all common base dependencies in the base image. This includes:

* WSGI libraries
* Flask and related plugins
* Development requirements

## Consequences

The image size increases (currently 553MB). Build times of child images go down.
For example, building the map-storage image without Docker cache takes 17
seconds.
