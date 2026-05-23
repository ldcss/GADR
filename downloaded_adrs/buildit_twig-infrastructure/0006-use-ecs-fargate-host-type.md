# 6. Use ECS FARGATE host type

Date: 2019-02-19

## Status

Accepted

## Context

AWS Bare Metal rig gives you the choice between EC2 hosting or FARGATE for compute.

## Decision

For the Twig riglet, we will use FARGATE.  Primary driver for this decision is to have a reference the uses FARGATE instead of EC2, and we are in the process of updating the Twig riglet.

## Consequences

Twig isn't an ideal candidate for FARGATE hosting because the smallest FARGATE memory choice is 512 MB which is more than enough for both twig (nginx) and twig-api (NodeJS).
