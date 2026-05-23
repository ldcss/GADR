# PowerShell Core 6 Deployment Scripts

## Status

Accepted.

## Context

Deployment requirements need to be expressed somehow—either declaratively or in a programming language.

## Decision

Individual Marain services express their deployment requirements in the form of a set of PowerShell scripts. These will be run in PowerShell core v6.

## Consequences

The advantage of a programming language over data structures is deployment scripts can make decisions if they need to. There's an automatic level of flexibility. PowerShell is a scripting language, meaning that there's relatively low complexity when it comes to getting things runnable—services don't need to build their deployment code, they just need to make script files available. Using PowerShell Core means we have the option to run on Linux.

The downside is that PowerShell gets a bit messy for anything non-trivial. You end up wanting to create modules, at which point you now need a means of installing the module (which also tends to complicate the development of the code that gets installed as a module).