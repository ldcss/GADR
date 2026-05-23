# Supported Node Versions

Date: 2017-12-15

## Status

Accepted

## Context 

eLife has projects built in Node.
 
eLife has projects that use the Node Package Manager (npm) in at least part of their own build process, even if the main technology of the project is not Node.

In order to provide language version consistency across projects we need to get a consensus on which Node versions we are going to support.

In order to provide dependency management consistency, we need a consensus on which npm versions to support.

Staying up to date with the major and minor versions of Node is important:

- to be able to use new features (nice to have)
- to keep working on a version that receives bug fixes and security updates (must have)            

## Decision

To use 8.x, the current Long Term Support (LTS) line.

In or around January 2019 to review upgrading to the next LTS line before 8.x drops out of active LTS in April 2019 (see [node release schedule](https://github.com/nodejs/Release#release-schedule)).

To use whichever npm version is bundled with the Node version we use.

When upgrading, we will make a concerted effort to upgrade all projects as part of the same piece of work.  


## Consequences

New projects should use the latest release in the 8.x line at the time they are started, subject to any project-specific constraints.

Existing projects should be upgraded to use the 8.x line before April 2018, when Active LTS for the 6.x line ends.

  
