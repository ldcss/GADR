---
layout: layouts/page.njk
title: ADR-0004 Use gherkin for describing acceptance tests
pageTitle: ADR-0004 Use gherkin for describing acceptance tests
pageDescription: We should determine how to develop and document our accptance tests.
path: /blueprint
permalink: /blueprint/adrs/ADR-0004-use-gherkin-for-describing-acceptance-tests.html
eleventyNavigation:
  parent: Architecture decisions
  key: ADR-0004 Use gherkin for describing acceptance tests
  order: 4
---

# 4. Use gherkin for describing acceptance tests

Date: 2020-03-30

## Status

Accepted

## Context

We should determine how to develop and document our accptance tests. This decision describes the choice around the langauge (DSL) that we use to describe them.

## Decision

We have determined to describe our acceptance tests using Gherkin.

## Consequences

Gherkin is a broadly used DSL for describing acceptance tests that has implementations across a range of programming languages.
