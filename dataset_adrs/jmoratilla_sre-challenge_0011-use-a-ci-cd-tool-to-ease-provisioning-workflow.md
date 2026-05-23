# 11. use a CI/CD tool to ease provisioning workflow

Date: 2020-06-01

## Status

Accepted

## Context


Time to work on the CI/CD solution.

I need a job manager to build, test and deploy the apps to the kubernetes
 cluster.

I know there is a lot of documentation about jenkins, but I have been working
in the last years with other solutions like:

* SolanoCI (now closed)
* CircleCI

So I need to see if there is a way to use my knowledge in CircleCI or not.
  Besides, CircleCI has a free plan very useful for testing.

I have tested Github Actions, it's similar to CircleCI.  Also I intended to use
 the Gitlab pipeline solution, but at the end I have no time to waste. 

## Decision

I'm going to try first CircleCI to see if I can deploy to AWS EC2.

## Consequences

Each time I run the workflow, the previous system should be deleted.  I prefer
 to ensure I'm working on a clear environment than handling a messed up system.