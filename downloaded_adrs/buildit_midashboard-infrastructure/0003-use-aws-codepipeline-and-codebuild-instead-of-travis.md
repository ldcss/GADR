# 3. Use AWS CodePipeline and CodeBuild instead of Travis

Date: 2017-09-27

## Status

Accepted

Amends [2. Use AWS Bare Metal Rig approach](0002-use-aws-bare-metal-rig-approach.md)

## Context

Travis has some limitations about what stages you can use to create a pipleine.  We still desire to have a hosted/PaaS CI/CD solution

## Decision

* Use AWS CodePipeline and CodeBuild instead of Travis
* We will aim to create a new Pipeline/Build and potentially execution environment per branch.
  * This will be manual at first and later could be automated via webhooks and lambda functions

## Consequences

* We don't know enough about CodeBuild/CodePipeline to understand whether it's the right fit or not.
* We've already found that CodePipeline is tied to a branch potentially making it hard to run pipelines for branches and PRs
* Creating environment per branch has the following consequences:
  * Assumes creating/tearing down environments is automated and relatively quick
  * Advantage: exercises our Infrastructure as Code regularly
  * Advantage: potentially offers complete isolation to run full suite of tests
  * Disadvantage: additional cost and potential resource limits
