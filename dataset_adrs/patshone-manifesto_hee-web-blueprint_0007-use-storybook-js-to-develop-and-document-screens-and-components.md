---
layout: layouts/page.njk
title: ADR-0007 Use storybook.js to develop and document screens and components
pageTitle: ADR-0007 Use storybook.js to develop and document screens and components
pageDescription: 
path: /blueprint
permalink: /blueprint/adrs/ADR-0007-use-storybook-js-to-develop-and-document-screens-and-components.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0007 Use storybook.js to develop and document screens and components
  order: 7
---

# 7. Use storybook.js to develop and document screens and components

Date: 2020-04-04

## Status

Accepted

## Context

As part of efforts to create a separation between the development of our content management and content delivery tiers and in order to support the development of a frontend framework that could be used across multiple delivery platforms, we sought to identify a tool to support a component based development workflow. We reviewed the following options:

### Options

#### Styleguidist - https://github.com/styleguidist/react-styleguidist

- **Pros:**
    - Provides great styleguide documentation
- **Cons:** 
    - Is restricted to React or Vue (for which there is an alternative project)

#### StoryBook.js - https://storybook.js.org/

- **Pros:**
    - Has support for a wide range of templating languages including HTML and Web Components as well as React and Vue
- **Cons:** 
    - Isn't really setup for serving associated documentation (ie less of a Design System tool)


#### PatternLab - https://patternlab.io/

- **Pros:**
    - Provides out of the box support for PHP templating such as Twig and Javascript templates such as Handlebars
- **Cons:**
    - Has taken a very long time to move from version 2 to version 3 and still doesn't appear to be stable

## Decision

We have chosen StoryBook.js as the component development tool to use for the HEE National Website platform. This choice was guided by the following:

- StoryBook's current usage across other NHS Digital projects
- StoryBook's support for a wide range of templating languages
- StoryBook's ability to provide automated testing for concerns such as accessibility

## Consequences

StoryBook provides support for a broad range of templating languages including vanilla HTML. It is already used by NHS Digital to manage the development of the React version of the NHSUK Frontend components. StoryBook provides a good way of encapsulating, testing and publishing the components that form the HEE Frontend.
