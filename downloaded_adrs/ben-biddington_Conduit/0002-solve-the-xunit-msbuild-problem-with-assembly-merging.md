# 2. Solve the Xunit/MsBuild problem with Assembly Merging

Date: 22/02/2016

## Status

Accepted

## Context

We have encountered probelms with the `xunit` task when run with `msbuild` (`xbuild works`) in that it is unable to locate required xunit assemblies. 

## Decision

This can be solved by copying the missing files to the same directory as `msbuild.exe` -- but this way may be easier to consume.

Merge the required assemblies into `Conduit.Adapters.Build.dll` or  `Conduit.Adapters.Targets.dll`

## Consequences

* Easier consumption: build file is not polluted with copying targets
