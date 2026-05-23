# 22. Use Auth0 for access management at scale

Date: 2018-09-04

## Status

Accepted

## Context

We need to give increasing numbers of suppliers access to the service, in order to deliver the framework transition plan. In November, we need to transition one or more frameworks with very large (1,000s) supplier user bases. Routine account management activities like changing the account email addresses, resetting passwords, and requesting new accounts, cannot be handled manually within the delivery team at this scale. Users need to be able to self-serve these activities, and internal users in the operational team need to be able to administer and support them without additional engineer involvement.

A permanent CCS-wide access management solution has not yet been agreed upon, and is therefore not ready for integration.

## Decision

We will use the paid tier of Auth0 to support this scale of suppliers.

## Consequences
We will need to continue to engage with the wider CCS work to choose and implement a common access management solution, so that we can prepare to integrate and migrate users when such a solution is in place.

We will need to consider the extent of our integration with Auth0 as an interim solution for which a permanent replacement is being sought.
