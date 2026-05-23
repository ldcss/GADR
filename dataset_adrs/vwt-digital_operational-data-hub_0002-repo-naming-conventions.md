# 2. repo naming conventions

Date: 2021-02-01

## Status

Accepted

## Context

We feel the need to use a naming convention for github repos.

## Decision

We identify three kinds of repositories:

### 1. General rules:
* Use hyphens ('-') between words in the name because:
    * words written together without something inbetween are unclear.
    * "\_" is harder to type than "-"  [stack overflow](ttps://stackoverflow.com/a/11947816).
* Make repo names not longer than needed. (Because GCP project names are also limited in length).

### 2. config VWT DAT repositories
Config repositories are repositories containing configurations of a specific Google Cloud Project (GCP) project.

* Should have the same name as the GCP project they are connected to minus the customer, environment and location.
* Name ends with `-config`.

### 3.  solutions VWT DAT repositories
Solutions repositories are repositories containing solutions, they can belong to multiple domains.
* Their names should always start with the domain they belong to.
* If the repository will handle multiple facets of the service, the name should end in `-handlers`
* Sometimes, two repositories are connected because they are the frontend and backend of a service. Their names should be the same except for the ending. Frontend repositories should end in `-tool` and backend repositories should end in `-api`.

### 4. "normal" VWT DAT repositories
"Normal" repositories are repositories not belonging to a solution. They contain code used specifically for the Operational Data Hub (ODH).
* Repository naming is equal to naming convention for solution repositories. Domains for these reposiitories is limited to `dat` and `odh`.
* If the repository is forked from another repository, its name should contain the name of the repository it forked from.

## Consequences
