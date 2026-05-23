# 2. Use AWS Bare Metal Rig approach

Date: 2017-09-27

## Status

Accepted

Amended by [3. Use AWS CodePipeline and CodeBuild instead of Travis](0003-use-aws-codepipeline-and-codebuild-instead-of-travis.md)

## Context

We need to create a riglet for our new twig project so that we practice what we preach.

## Decision

We will use the AWS Bare Metal Riglet from bookit-infrastructure as a starting point for our riglet.  We will keep the previous twig-riglet and create a new twig-infrastructure project/repo.
Technologies:

* AWS: CloudFormation, ECR, ECS, Route53, VPC, ALB
* Deployment Mechanism: Docker images
* Build: CodePipeline, with Jenkins as an eventual target

## Consequences

* This will tie us to the AWS platform.
* The twig-riglet is not "complete."  There a number of improvements that can be made along the way that we will have to balance with feature work.
