# 1. Folder structure

Date: 2019-04-10
Modified: 2019-05-21 (Tyson)

## Status

Accepted

## Context

Having a fixed structure for a project has may advantages, limiting spread of files across multiple folders and contraining locations to known places. THere is an advantage is letting a folder strucute emerge oganically, but also a large risk, as things can break when low-level file locations change, necesitating logs of bug fixing and refactoring. Having a rigid initial structure canb lead to later restrictions, or imposed complexity.
## Decision

The following folder strucure is adopted:

    .
    ├── app
    │   ├── controllers
    │   ├── models
    │   ├── public
    │   │   ├── css
    │   │   ├── img
    │   │   └── js
    │   ├── routes
    │   └── views
    ├── docs
    │   ├── adr
    │   ├── misc
    │   ├── project_artifacts
    │   └── templates
    ├── node_modules
    ├── test
    └── local_only

**Update** Removed folders originally specified that were found to not be required during project development: 'log' and 'utility'

## Consequences

Will need to be disciplined in file locations and naming conventions. Will need to produce a naming convention document to accompany this folder structure ADR.

 * local-only will not be on repo
 * node_modules MUST not be on repo
 * utility -> back-end, maintenance task folder, not related to site or site-serving
 * docs must be maintained : directly to main branch, or updated in seperate branch?
