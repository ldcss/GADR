# 4. Use multiple projects

Date: 2019-10-19

## Status

Accepted

## Context

The software could be developed in one big (Gradle) project.  
This would make integration easier.  
At the same time this would make re-use of the code outside of this project harder.  
One big project would probably lead to worse code since there would not be the need to have defined API boundaries.  

## Decision

We will try to modularize the software and will use multiple projects to achieve this goal.

## Consequences

Changes in one module might have unexpected side-effects on other modules.