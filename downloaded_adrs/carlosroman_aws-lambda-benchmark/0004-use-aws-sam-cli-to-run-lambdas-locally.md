# 4. Use AWS SAM CLI to run Lambdas locally

Date: 2019-05-03

## Status

Accepted

## Context

The make it easier to debug the code without deploying we need a way to run all the Lambdas locally.

## Decision

As we are already using the [AWS Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model) to define our serverless application we can use [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli) to run things locally.
By wrapping up AWS SAM CLI in a Docker container we can also use (Docker Compose)[https://docs.docker.com/compose/] to spin up our stack locally.
With Docker Compose we can spin up DynamoDB locally and API gateway so that we can invoke the Lambdas as if they were deployed.

## Consequences

We can now run acceptance tests locally.
This means that the same tests we write to run against our local stack could be run against a deployed one.
The problem with this change is that we now have to be careful how we structure our code.
Due to the fact that SAM CLI uses Docker means that we can run into issues when accessing code/libraries that are not mounted correctly. 
This may cause issues when running Lambdas that rely on certain files being in a particular directory (like the `node_modules` directory).
If anything uses a symlink it could end up pointing to a file/directory that has not been mounted in Docker.
