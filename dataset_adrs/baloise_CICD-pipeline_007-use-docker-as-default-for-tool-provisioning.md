# 7. Use docker as default for tool provisioning

Date: 2020-11-20

## Status

In progress

## Context

1) There different provisioning mechanisms for build tools
  1) [Jenkins global tools](https://wiki.jenkins.io/display/JENKINS/Manage+global+settings+and+tools+installations)
  1) [Docker containers](https://hub.docker.com/)
  1) Tool specific managers like [jEnv](https://www.jenv.be/) or [SDKMan](https://sdkman.io/)
1) We want to ensure a [homogeneous build across environments](006-homogeneous-build-across-environments)

## Decision

We use docker as default for tool provisioning

## Consequences

Linux or Docker for Windows is required as development platform.