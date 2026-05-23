# 10. Use travis ci for continuous integration

Date: 2019-10-20

## Status

Accepted

## Context

We want to use continuous integration to make sure that at any time the build is working.  
CI will check every commit and PR.  
Possible choices are: Travis CI, CircleCI or AppVeyor.  
Travis CI offers Linux and Mac builds. Windows is in beta.  
CircleCI supports all 3 platforms.  
AppVeyor supports Linux and Windows.  
The authors have already used Travis CI.  

## Decision

We will use Travis CI for continuous integration.  

## Consequences

Possible vendor lock-in.
