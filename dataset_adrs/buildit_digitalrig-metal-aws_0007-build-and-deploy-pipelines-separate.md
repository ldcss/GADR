# 7. Split Pipeline into Distinct Build and Deployment Pipelines

Date: 2019-01-14

## Status

Accepted

## Context

In the previous iteration, build and deploy were consolodated into one pipeline. The result of this being that any type of configuration change required a full rebuild to deploy.  This could become unwieldy with projects that have a long-running build step.

## Decision

Pipeline has been split into distinct build and deploy pipelines.  The build pipeline, in addition to the image that it uploads to ECR, exports artifacts build.json and src.zip.  Src.zip is required still required in the deploy pipeline to run integration tests.  In the deploy pipeline, either the artifacts supplied by the build pipeline OR new app.yaml templates will trigger the pipeline.  Consequently, a config change may be made by uploading a new app.yaml, without having to re-build the Docker image.

## Consequences

A less-than-desirable consequence of this is that the stack must be rolled out with the transition to the Integration stage disabled in the deploy pipeline.  If it were not, under certain circumstances, the deploy pipeline could be executed, upon stack rollout, before the ECR image is built.  After the build pipeline succeeds for the first time, the deployment pipeline may have all its transitions enabled, and should be available without issue for continued use.
