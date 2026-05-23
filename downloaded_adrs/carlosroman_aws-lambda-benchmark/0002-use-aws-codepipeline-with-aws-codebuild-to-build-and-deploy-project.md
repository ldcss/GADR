# 2. Use AWS CodePipeline with AWS CodeBuild to build and deploy project

Date: 2018-08-07

## Status

Accepted

## Context

The project needs a way to be built and deployed. It needs to be quick and easy to use so has to be able to pick up changes to the git repo. It should be easy for anyone recreate the workflow used here and flexible enough to handle building multiple languages. At the end of successful build the artifact should get deployed.

## Decision

As this is project is benchmarking AWS Lambdas it makes sense to use the services AWS has for building (AWS CodeBuild) and deploying (AWS CodePipeline) code.

## Consequences

Using AWS CodePipeline and CodeBuild allows us to create our CI/CD pipepline as code. This means anyone can fork the repo and deploy a pipeline to their AWS account. They'll also be able to deploy the Lambdas and API gateway using the pipeline created.

Doing this as code will mean that the task for creating a CI/CD pipeline for building and deploying will take time. On the plus side, once done we will have a recreatable build and deployment of the pipeline.

