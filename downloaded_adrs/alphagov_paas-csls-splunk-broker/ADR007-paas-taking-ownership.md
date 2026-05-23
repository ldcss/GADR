# ADR006: GOV.UK PaaS taking ownership

## Context
The RE Autom8 team originally wrote and maintained this broker, in collaboration with Cyber Security. It is configured as a service broker in the Ireland and London regions of GOV.UK PaaS, and enabled for a few GDS-internal tenants. The code lives in a subdirectory of the `alphagov/tech-ops` repository, and the pipeline which builds and deploys it lives in the Tech Ops multi-tenant Concourse.

## Decision
The GOV.UK PaaS team decided that they were happy to take ownership of the broker, because it requires knowledge of the platform to maintain, and they maintain all the other brokers on the platform.

## Consequences

The code has been extracted from the subdirectory of the `alphagov/tech-ops` repository, and has been set up in its own repository: `alphagov/paas-csls-splunk-broker`.

The Concourse pipeline now points to this repository, but the GOV.UK PaaS team decided to continue running it in the Tech Ops multi-tenant Concourse, because it would be difficult to move and be of little value to do.

As a result, the Concourse pipeline for this repository continues to run at https://cd.gds-reliability.engineering/teams/cybersecurity-tools/pipelines/csls-splunk-broker. 
