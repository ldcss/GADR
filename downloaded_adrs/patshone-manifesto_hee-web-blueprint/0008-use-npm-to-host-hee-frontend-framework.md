---
layout: layouts/page.njk
title: ADR-0008 Use npm to host HEE frontend framework
pageTitle: ADR-0008. Use npm to host HEE frontend framework
pageDescription: 
path: /blueprint
permalink: /blueprint/adrs/ADR-0008-use-npm-to-host-hee-frontend-framework.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0008 Use npm to host HEE frontend framework
  order: 8
---

# 8. Use npm to host HEE frontend framework

Date: 2020-04-04

## Status

Accepted

## Context

We need to identify how and where we will store packages that describe our front end framework. There are a number of NHS UK and NHS Digital projects that already use NPM as their package repository for front end code.

## Decision

We have chosen to store our packages on NPM. 

## Consequences

NPM requires the least effort to setup, is free for open source projects and is already in use for other NHS projects so provides an infrastructure choice that should be well understood.
