# 6. Manage build with Gradle

Date: 2018-12-27

## Status

Accepted

## Context

`menu-generation` application will use the Spring framework along with other third party libraries, thus requires a
dependency management tool.

Effective development lifecycle requires Continuous Integration, thus a build management tool is necessary.

[Gradle](https://gradle.org/) is one of the two main build management tools for the Java ecosystem with [Maven](http://maven.apache.org/).
Gradle is considered as more extensive and quicker than Maven. It is also well integrated with many tools, including
the Spring framework.

## Decision

Gradle will be used to manage project dependencies and build tasks.

## Consequences

Gradle will provide the dependencies management through default Maven Central repository. Existing plugins provided by
the open-source community will help defining the build tasks easily.

Acceptance testing build lifecycle will take advantage of the Gradle extensible model.

Gradle may help splitting the `menu-generation` application into multiple modules when required.
