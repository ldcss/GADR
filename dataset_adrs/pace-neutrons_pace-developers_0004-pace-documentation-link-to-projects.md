[<-previous](0003-pace-projects-will-have-independent-documentation.md) | [next->](0005-pace-projects-must-be-semantically-versioned.md)

# 4. PACE documentation link to project documentation

Date: 2020-Jun-20

## Status

Accepted

## Context

The PACE project is a collection of independently developed and released tools. These tools are built in different technologies. 

Creating a single "global project documentation" release would introduce a tight coupling between the projects and create complexities around supporting multiple versions of documentation at a project level.

GitHub pages provide an "organization" level documentation page. For PACE this will be at https://pace-neutrons.github.io. The documentation is displayed from a single folder or branch in an associated GitHub repository. 

## Decision

The organization-level documentation will provide a "high-level" overview of the project and contained tools, with links to the project-specific documentation URLs.

## Consequences

- The PACE project documentation will rarely change and provide a single landing page for users accessing the project.

- The individual PACE tools are not constrained in their release process

- There is no need to create a complex "merge" of documentation section from projects into one single document repository as part of the build processes