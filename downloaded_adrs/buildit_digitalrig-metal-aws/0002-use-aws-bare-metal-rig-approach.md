# 2. Use AWS Bare Metal Rig approach

Date: 2017-09-27

## Status

Accepted

Amended by [3. Use AWS CodePipeline and CodeBuild instead of Travis](0003-use-aws-codepipeline-and-codebuild-instead-of-travis.md)

## Context

We need to create a riglet for our new bookit project so that we practice what we preach.

## Decision

We will use the AWS Bare Metal Riglet from bookit-riglet as a starting point for our riglet.  We will keep the previous bookit-riglet and create a new bookit-infrastructure project/repo.
Technologies:

* AWS: CloudFormation, ECR, ECS, Route53, VPC, ALB
* Deployment Mechanism: Docker images
* Build: Travis

## Consequences

* This will tie us to the AWS platform.
* The bookit-riglet is not "complete."  There a number of improvements that can be made along the way that we will have to balance with feature work.
