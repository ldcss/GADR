# 2. Use ACF PRO

Date: 2020-08-13

## Status

Accepted

## Context

The themes and plugins we make often need to add fields to the admin interface.

We've been using ACF PRO on nearly every new site we've made in the past few years, and we've used the free version of ACF for perhaps 5-7 years. We're comfortable with it and it's proven its stability and usefulness.

## Decision

Install ACF PRO on every site we create. If we don't need it, we can remove it before deployment.

To add a field to a theme or plugin we should copy the PHP code and paste it into the codebase.

## Consequences

Using ACF PRO has been a huge benefit to every site we've used it on.

Adding fields via PHP code rather than storing that in the database means that development environments are quick and easy to set up.
