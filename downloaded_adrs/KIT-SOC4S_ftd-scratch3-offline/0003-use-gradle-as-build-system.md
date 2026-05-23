# 3. Use Gradle as build system

Date: 2019-10-19

## Status

Accepted

## Context

Modern software needs to be easy to build.  
For this reason most software uses a build system to specify how the software is build and which dependencies it needs to work.  
Popular build systems in the Java world are Ant, Maven and Gradle.  
Ant is pretty flexible but lacks dependency management and is also very rarely used these days.  
Maven is more rigid than Ant but supports dependency management and is still widely used.  
Gradle is the newest build system. It can be programmed in Groovy/Kotlin and is the most flexible build system.  
Gradle is also the only way to build for the Android platform.  
Gradle enjoys widespread usage and the authors are most proficient in it.

## Decision

We will use Gradle as build system.

## Consequences

Gradle's flexibility makes it easy to add custom tasks and to accommodate to changes.  
Gradle's flexibility makes troubleshooting harder at the same time.  
Gradle has a steep learning curve and time will have to be spent to learn it.  