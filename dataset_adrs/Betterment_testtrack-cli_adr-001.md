# ADR 001: Resources referring to splits not in schema require validation opt-out

## Status

Accepted

## Context

Because we're deprecating fully-loaded local TestTrack server instances
in favor of the testtrack CLI, client-side validations are the only way
of ensuring that migrations will apply cleanly in production.

We're entering a world where developers will likely not have local
copies of all the app repositories that might contribute splits to
TestTrack's configuration fully updated at all times, making validating
split names locally across apps impossible and undesirable to attempt.

So we're seeking to find a balance that can validate as much as we can
while accepting the fact that cross-app split dependencies won't be
validatable locally.

## Decision

feature_completions and remote_kills of splits defined by other apps
will not be validated, but you'll have to opt out in one of a few ways
in order to skip validation:

* Choose a split name prefixed with another app's name (a new-style
  split), which indicates that validation of split presence is
impossible.
* Specify a legacy non-prefixed split name with the `--no-prefix`
  option.  Non-prefixed splits names will not be validated for presence
in the schema because they are not obviously tied to any app in
particular, so even though a non-prefixed split might belong to our app,
it's not a certainty, and impossible to validate.
* Specify that you know that a split name doesn't appear in the schema
  and you want to write a migration referring to it anyway via the
`--force` option. This is important in the case of
creating/modifying/destroying remote kills or feature_completions for
retired splits which no longer appear in the schema file due to their
retirement.

## Consequences

It will be possible to opt out of split name validation in one of these
ways and create a migration that will fail to apply in production
because of a typo'd split name. The hope is that these issues will not
arise frequently, but if it's painful we will find out quickly and can
adapt. One option would be to soft-link feature_completions and
remote_kills to splits by name so that if typos arise, the build/deploy
pipeline doesn't jam up.
