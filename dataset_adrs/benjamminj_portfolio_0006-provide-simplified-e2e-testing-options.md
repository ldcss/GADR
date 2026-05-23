# 6. Provide simplified e2e testing options

Date: 2020-10-23

## Status

Accepted

## Context

End-to-end tests should be easy to run, and possible to run in a variety of use cases.

Until [Playwright test runner](https://github.com/microsoft/playwright-test) is a little more stable, we want to set this up within Jest.

## Decision

Playwright will be configured to support the following test modes:

- **`dev` (default)**: Playwright will run tests in a headful chromium browser with the devtools enabled. Good if you need to debug tests or see them being executed.
- **`headless`**: Playwright will run tests in a headless chromium browser only. Good if you're practicing some TDD and want to run the suite often and quickly.
- **`browsers`**: Playwright will run in headless mode, but it will run every end-to-end test in `chromium`, `firefox`, and `webkit`.
- **`devices`**: Playwright will run in headless mode with chromium only, but it will run every end-to-end test on all `iPhoneX` and `Pixel 2` screen sizes.

## Consequences

- When devving, I'm hoping that having it be easier to run playwright will result in running the e2e tests more as part of my workflow.
- This will open up the ability to run browser _and_ device testing during CI.
- Simpler, easier-to-understand config file.
