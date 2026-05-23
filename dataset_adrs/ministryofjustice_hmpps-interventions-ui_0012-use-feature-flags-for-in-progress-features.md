# 12. Use feature flags for in-progress features

Date: 2021-09-13

## Status

Accepted

## Context

There are a few reasons we might not want to put a new feature in front of users as soon as it's been merged into the `main` branch:

- The API might not be up-to-date with the latest version of the UI (and vice versa) - because we're building the UI and API side of the service independently, there are times when the two may be out of sync: an endpoint may not yet be providing all the data we need; the backend functionality may not be finished at the time of writing the UI code.
- We want to satisfy the Pact contracts between the two sides of the service but not use the new data structure until the UI has been updated.
- The new functionality may need to be further tested (either with users by developers) and iterated upon before release.
- We want to keep Pull Requests as small as possible so they're quick to review and it's easy to make changes - this means we'd want to merge smaller chunks of work at a time, which might not be ready for users.
- We want to test interactions between systems (e.g. the Community API) on the Development environment but not release these changes to the public.

## Decision

Any features or behaviour that isn't ready to be interacted with by users will be placed behind a config-based feature flag, configured in `server/config.ts`, e.g. as below:
```
features: {
  previouslyApprovedActionPlans: get('FEATURE_PREVIOUSLY_APPROVED_ACTION_PLANS', 'false') === 'true',
}
```

This can then be turned on for each environment by adding the environment variable (e.g. `FEATURE_PREVIOUSLY_APPROVED_ACTION_PLANS`) to the intended environment.

We'll usually want to enable this for the development environment and test environment, possibly the pre-prod environment but not the production environment.

Before deploying the changes to the production environment, it's a good idea to double check the configuration is as expected e.g. by checking it's hidden in the pre-production environment.

Once the feature is ready to be interacted with by users, we'll remove the feature flag from the UI configuration.

## Consequences

- Pull requests can be kept small and self-contained, as we don't need to release a whole feature at once, and there's no risk of it being visible to users.
- We can test functionality on the development environment without these changes being deployed to production.
- We can release changes to the contracts between the UI and API but keep existing functionality working until both are in sync.
- We can test functionality in User Research sessions without it being on the production environment.

There's a small overhead involved in setting up the config and testing it's visible or not on the desired environment.
