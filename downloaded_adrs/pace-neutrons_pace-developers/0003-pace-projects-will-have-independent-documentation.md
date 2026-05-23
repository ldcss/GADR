[<-previous](0002-use-github-pages-for-user-documentation.md) | [next->](0004-pace-documentation-link-to-projects.md)

# 3. PACE Projects will have independent documentation

Date: 2020-Jun-20

## Status

Accepted

## Context

PACE contains a number of independently developed and released projects with separate source and build pipelines.

Coordination of documentation from projects using three different primary languages (MATLAB, Python, C) with varying release cycles will create tight coupling between the projects and their builds.



## Decision

Each project will maintain its own GitHub pages documentation that will be updated with the project's build-release-deploy pipeline.



## Consequences

- Project specific documentation will be directly accessible e.g. https://g5t.github.io/brille or https://pace-neutrons.github.io/euphonic 
- There will be no single landing page for PACE project documentation
- If consistent style and layout is required between the projects this must be managed as the document configuration will be repeated across each project