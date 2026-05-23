---
layout: layouts/page.njk
title: ADR-0005 Use selenide for creating and managing acceptance tests
pageTitle: ADR-0005 Use selenide for creating and managing acceptance tests
pageDescription: We need to choose a framework to write our acceptance tests in
path: /blueprint
permalink: /blueprint/adrs/ADR-0005-use-selenide-for-creating-and-managing-acceptance-tests.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0005 Use selenide for creating and managing acceptance tests
  order: 5
---

# 5. Use selenide for creating and managing acceptance tests

Date: 2020-03-30

## Status

Accepted

## Context

Having determined to use Gherkin as the way that we describe our acceptance tests, we need to choose a Java based (because BloomReach is Java based) framework to write our acceptance tests in.

## Decision

We have determined to use Selenide as the framework to implement our automated tests.

## Consequences

Selenide provides a layer over Selenium which mitigates and manages some of the risks/problems with using Selenium. It provides a fluent API for describing tests and is simple to configure.
