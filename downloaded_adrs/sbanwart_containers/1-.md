
# 1. Use Ubuntu minimal for container base image
======
Date: 26-04-2020 20:31:01

## Status
======
Proposed

## Context
======
The existing container images use a variety of base images, including Fedora and Alpine Linux. These base images have different sizes, and different behavior that can cause various issues.

## Decision
======
We should use a common base image for building container images. The base image that looks the most promising is Ubuntu minimal.

## Consequences
======
Container creation should be easier with a consistent base image. With the single base image, the tooling needed to create users, install packages, etc. is the same across all container images. Existing Dockerfiles will need to be revised to use the Ubuntu tools and commands.

