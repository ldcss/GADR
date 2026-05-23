# Documentation Structure

## Context and Problem Statement

We want to have a well defined structure for what to document where.


## Considered Options

* Everything in docs repository
* Everything in mico repository
* Leave it as is (mostly in docs repository & code documentation in mico repository)


## Decision Outcome

Chosen option: Leave it as is.

### Clarification for what to document where:

#### Docs Repository

Rationale: If I want wo use mico this documentation should contain all I need to know.

Examples:

* Design Decisions
* Architecture
* Component descriptions (mico-core, mico-admin, mico-grapheditor)
* API Interfaces (REST Api, etc.)
* How To's (How To install mico, How To use mico, etc.)

#### Mico Repository

Rationale: If I want to change something in the code this documentation should contain additional information about code specifics.

* Javadoc, Typedoc, etc.
* Descriptions for important classes and how to use them
* How to write a new REST Endpoint, Unit Test, Plugin, etc.
* Links to dependencies (with documentation), relevant documentation in docs repo

If possible use links to the relevant documentation instead of describing the whole thing.


## Everything in docs repository

### Docker out of Docker

* Good, because of clear seperation of documentation and code
* Bad, because sphinx can use language native documentation (like javadoc) only if code is in the same repository

### Everything in mico repository

* Good, because one repository for everything
* Bad, because the workflow for documentation (without pull requests) and the workflow for code changes (with pull requests) oppose each other

### Leave it as is (mostly in docs repository & code documentation in mico repository)

* Good, because it enables fast documentation workflow without pull requests
* Good, because seperate code documentation still supports javadoc, etc.
* Good, because built documentation still feels like one if interlinked properly
* Bad, because it needs explanation for what goes where
