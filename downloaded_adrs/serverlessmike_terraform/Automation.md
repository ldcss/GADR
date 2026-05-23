# Automation

Date: 02/10/2019

## Context

Services that we are in the process of migrating or that have recently competed migration are likely to go through a period of needing more maintenance that a mature service.
One answer to this is to handle all such problems on a case by case basis, fixing as we go in order to try to keep the velocity as high as possible. At the other end of the scale is to drop a significant cost on the project by automating all such processes.

## Decision

We will automate every process possible. Where an automated process may be applicable to more than one server, then we will attempt to write the solution to be DRY.

## Consequences

The project will take longer and cost more, but leave behind much less technical debt.
