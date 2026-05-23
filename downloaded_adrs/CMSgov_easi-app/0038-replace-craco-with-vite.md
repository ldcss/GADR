# Migrate from Create React App & Craco to Vite

**User Story:** [EASI-3082](https://jiraent.cms.gov/browse/EASI-3082)

Meta (the organization who created React) has formally stopped recommending that developers use Create React App. The reasons won't be enumerated here in perfect detail, but this [Pull Request](https://github.com/reactjs/react.dev/pull/5487) on the official React docs site is a good place to start if you want more context.

Given this recommendation, and with the fact that Vite promises (and delivers) faster compilation times, we have considered (and settled on) migrating the application to Vite.


## Considered Alternatives

* Stay on CRA/Craco
* Migrate to Vite

## Decision Outcome

* Chosen Alternative: **Migrate to Vite**

This approach, while a heavy lift, should provide us with faster compilation, better support, and a more modern toolchain.

## Pros and Cons of the Alternatives

### Stay on CRA/Craco

* `+` No config changes to make
* `+` CRA is a popular tool, despite its age and limitations
* `-` Less efficient (larger) bundle sizes
* `-` Much slower compilation times

### Migrate to Vite

* `+` Faster build times
* `+` More active support and development
* `-` Requires a lot of trial and error to migrate, with potential breaking changes
