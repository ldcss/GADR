
# 2. Use fedora-minimal for container base image
======
Date: 24-04-2021 15:51:00

## Status
======
Accepted

## Context
======
Fedora has minimal base image too, and it will typically have more current versions of any software we need compared to the Ubuntu images.

## Decision
======
Change all Dockerfiles to use the latest `fedora-minimal` image as the base and update any necessary commands to work with Fedora system tools like `dnf`.

## Consequences
======
This will give us the benefit of using a common container image along with ability to keep the base image and dependencies updated.

