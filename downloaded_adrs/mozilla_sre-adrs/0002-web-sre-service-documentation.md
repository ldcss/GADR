# 2. Web SRE Service Documentation

Date: 2021-06-01
Scope: Web SRE Team

## Status

Approved

## Context

The Web SRE Team manages a number of services that vary in users, technologies used, setup, our commitment, infrastructure, process, etc. 

Pre-existing documentation for these services, if it exists, also varies - in location, level of detail, scope, structure, presumed audience, etc.

To help share knowledge between the Web SRE Team about these services' unique situations, a consistent baseline for our services documentation is a required first step.

## Decision

A Web SRE service here is defined as any codebase where we have some ownership over an aspect of this codebase being functional - e.g. the deployment process, automation, infrastructure running the service, observability of some aspect(s), or authoring the code ourselves. Web SRE services could be externally or internally-facing, including infrastructure services only Web SRE are aware of and leverage. Web SRE services also include non-prod environments for testing infrastructure code (like staging Kubernetes clusters to test building new clusters) and supporting services (log aggregation, alerting, etc) as well as non-prod application code. 

For each Web SRE Service, we will author a Service Documentation page in Mana as a child of https://mana.mozilla.org/wiki/display/SRE/Service+Documentation.

Service Documentation pages:
* use the Web SRE Services Docs confluence page template for its structure;
* have a primary audience of the Web SRE Team itself, with a secondary audience of other SRE teams;
* are open to Mozilla internally, however not all teams of Mozilla are the intended audience of these pages (SRE-external teams will focus on the escalation path section primarily);
* have Runbook pages (what to do when a specific symptom of an issue is recognized) as child pages to the relevant Service Documentation page;
* have How-to pages (how to perform specific tasks for a service) as child pages to the relevant Service Documentation page;
* are maintained to reflect the current state - to the best of our knowledge - of a service's context, including a service being decommissioned (the Service Documentation page should note that but be left up as a tombstone marker of the decision);
* cover Web SRE Services as defined above.
* replace SRE_INFO.md files in Web SRE team-managed source code GitHub repositories. When an SRE_INFO.md file is encountered, it should be reviewed for any information that can be added to a Service Documentation page, removed, and an link to the Service Documentation page added to the codebase's REAMDE.md.

Service Documentation pages do not:
* include all possible services Web SRE might work with - e.g. we don't document AWS Services generically or services owned and maintained by other teams; 
* include all possible details for all audiences beyond SRE - when such documentation requests come up, they can be added as a How To as a child to a service page, or a generic How To if not limited to one service;
* live anywhere other than Mana. Web SRE Service documentation managed elsewhere, e.g. GitHub, Google Docs, should be migrated & then deprecated via links pointing readers to the Mana page;
* replace other forms of documentation living elsewhere - e.g. codebase-specific documentation within a git repository, decision records in this repository, collaboration / draft developer notes in Google documents, Mana pages in other places and formats walking through shared infrastructure or processes, etc..

Service Documentation pages optionally have Runbook & How-To child pages. For these, there are the following expectatiosn:

Runbook pages should:
* include ways to validate what state a system is in (e.g. how to reproduce the problem);
* be as self-contained as is feasible;
* explain what problem a given state indicates;
* give commands to resolve the problem as clearly as possible;
* outline a fallback plan (who to call, what to do next).

How-to pages should:
* repeat existing documentation as little as possible. Linking to external docs is encouraged, perhaps augmented with our specific contexts;
* assume a high level of competence from the audience (don't explain how to download a csv file, though giving an example command to establish context is great);
* explain the decision points in a process, and how to make them;
* outline what is needed to perform the work as early as possible in the document (what access, what tools);
* outline who needs to approve the work, or how to decide if it's safe to do the work as early as possible.

## Consequences

This will require a fair amount of work in getting the Web SRE Services portfolio adequately covered by the guidelines above.

This will also require maintenance work ensuring the drift between service state and documentation state is as minimal as is feasible.

## Resources

* [Service Documentation Folder](https://mana.mozilla.org/wiki/display/SRE/Service+Documentation)
* [Web SRE Service Documentation Template (Web SRE Team & Jira Space admins only can view)](https://mana.mozilla.org/wiki/pages/templates2/viewpagetemplate.action?entityId=131596432&key=SRE)
