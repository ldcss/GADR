# 10. Feature Toggles

Date: 2017-10-22

## Status

Accepted

## Context

When releasing some features, we might want to only make them available to a sub set of users initially, to gain feedback and reduce the potential impact of bugs.

We also want to be able to continue development of a feature in master over a longer period of time, without it being available in an unfinished state.

## Decision

We will associate a set of feature toggles with a Pocket Account. 

## Consequences
Feature toggles for a user can be used by the frontend and backend to determine whether certain features are available to that user.

The frontend will need an endpoint from which it can periodically retrieve the feature toggles for a user.

Feature toggles will need to be removed once functionality has been deemed stable enough to give access to all users.

Application-wide feature toggles would require a toggle to be added for each user (and be added for new users). If this functionality is required,
it will most likely require additional work.
