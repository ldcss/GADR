# 9. Use Selenium for feature and end to end testing

Date: 2019-10-13

## Status

Accepted

## Context

We want to be able to run feature and end to end tests in browsers and as part
of continuous integration. We only want to write tests once, and have them run
in all environments.

[Selenium WebDriver](https://docs.seleniumhq.org/projects/webdriver//) is a
browser automation framework. It supports all major browsers and is supported by
cloud based browser testing services like
[BrowserStack](https://www.browserstack.com/).

## Decision

Use Selenium WebDriver to write feature and end to end tests via Jest.

## Consequences

Using Selenium, we can be more confident that the application we're building
will run as expected in browsers.
