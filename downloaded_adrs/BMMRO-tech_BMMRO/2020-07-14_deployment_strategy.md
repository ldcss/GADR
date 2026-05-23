# Deployment Strategy

**Status:** Accepted

## Context

Currently we only have one environment, development, and every change that is merged with master is deployed to this environment. Since we want developers to be able to continuously integrate their changes without interfering with the web application that is being used by our users, we decided to create two other environments, UAT (user acceptance testing) and production.

## Decision

Since we were already using Github Actions to deploy to the development environment (due to the fact that it's free and easy to configure), we decide to use it to deploy to the new environments too.
These were the different options considered for the deployment strategy for the different environments:

### Option 1 - One branch for each environment

In this approach each environment would have its own branch, and we would merge when we wanted to promote to a specific environment.
The flow would be the following: push to master => deploys to dev; merge with user-testing branch => deploys to user-testing; merge with production branch => deploys to production.

Problems with this method:

- App built separately for each environment
- No clear rollback method
- Three different ‘versions’ of code
- Greater complexity in git history
- Non-standard - Open source project so should not be too complex for contributors

### Option 2 - Manual triggers for each environment

There are two possible flows for this approach:

1. Push to master => deploys to dev; Create a pre-release => deploys to staging; Update pre-release to release => deploys to staging
   The problem with this approach is that it's very easy to make a mistake and do a release instead of a pre-release in the GitHub UI.

1. Push to master => deploys to dev; Create a tag => deploys to staging; Publish a release => deploys to staging
   The problem with this approach is that developers can add tags to branches too. So, if the trigger to deploy to production is the creating of a tag named "prod-deploy", and if a developer pushes a "prod-deploy" tag to a branch, that would trigger a deployment to production.

In both cases we could do a rollback by tagging an old commit and doing a release with that tag.

### Option 3 - Code pushed to master is deployed to all environments

The flow would be the following: Push to master => deploys to dev, user testing and production.
Feature toggles would be used to disable new features in production until approval.

Problems with this method:

- Would need to store production, UAT and development environment variables in build
- This would mean production users would be able to see details for all environments we have
- Each push to master would deploy to production, if a bug was introduced this would go directly to production
- Deployment time would increase
- For partial rollback, features could be toggled off.

### Final Decision

We've decided to use an approach similar to Option 2.
The flow is the following:

- Push to master. Code auto deployed to development environment and 'dev-deployed-XX' tag added
- Run local deploy script passing the environment ('uat') and the build to deploy ('dev-deployed-XX'). This adds a "uat-pending-XX" tag, that is updated to "uat-deployed-XX" once the deployment to that environment is successful.
- Run local deploy script passing the environment ('prod') and the build to deploy ('uat-deployed-XX'). This adds a "prod-pending-XX" tag, that is updated to "prod-deployed-XX" once the deployment to that environment is successful.

To rollback the local deploy script could be run passing 'prod' and an older build tag e.g. 'dev-deployed-11'. It may be enforced that any build must be deployed to UAT before production. In this case to rollback you would first need to deploy an old build to UAT then deploy UAT to production.

The cons of this approach are:

- Application is built every time we deploy to a new environment (as opposed to build an artifact once and promote it to the different environments).
- If the tags that trigger deployments ("uat-pending-XX" and "prod-pending-xx") are added to a branch, that would trigger a deployment too.

Despite the issues mentioned above, we've decided to use this approach due to time constraints but have created a new Github issue to investigate how to use artifacts.

## Links

- [Github Issue - Investigate different deployment strategies](https://github.com/BMMRO-tech/BMMRO/issues/24)
- [Github Issue - Create UAT and Production environments](https://github.com/BMMRO-tech/BMMRO/issues/60)
- [Github Issue - Investigate how to use artifacts with GitHub Actions](https://github.com/BMMRO-tech/BMMRO/issues/61)
