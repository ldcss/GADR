# 7. switch-tests-to-playwright

Date: 2021-10-06

## Status

Accepted

## Context

Cypress is currently ubiquitous in the end-to-end testing game, but there's a lot of things lacking.

Personally, I've been excited about [Playwright](https://playwright.dev/) for quite a while now, and I think it has the potential to unseat Cypress as a de facto e2e testing solution. Previously, the lack of a test runner made Playwright difficult to use as a testing framework — it was better suited to general-purpose browser automation. However, the addition of `playwright-test` changes this up.

I'm using my website as a trial run of what Playwright can do and whether it holds up to Cypress as a general testing solution. 🤞

## Decision

Replace existing Cypress tests with end-to-end tests written in Playwright.

## Consequences

- **Cross browser testing.** Cypress allows cross-browser testing, but not nearly as easily as Playwright does. I anticipate testing all modern browser engines will become much easier.
- **Learn a new tool.** I've always been bullish on Playwright since v0, so excited that it's now in a stable v1.
