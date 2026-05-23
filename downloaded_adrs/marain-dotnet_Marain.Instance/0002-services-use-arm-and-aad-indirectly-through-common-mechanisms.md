# Services use ARM and AAD indirectly through common mechanisms

## Status

Accepted.

## Context

Historically, our automated deployment scripts have tended to include a large amount of common boilerplate. This is partly because they are self-contained—they can typically be run on their own to perform a deployment. And it is partly just because they originate from what the Visual Studio tooling creates.

The problem with this is that it makes the project-specific details hard to spot. When looking at a sea of code that's almost identical to every other project, it's hard to see what it's doing that is in any way different from everything else.

## Decision

With `Marain.Instance`, deployment scripts in individual services do not communicate directly with either ARM or Azure AD. (They should not even be aware of what mechanisms are being used to perform this work—they should not need to know whether we are using the PowerShell Az module, the az CLI or even custom library code to talk to Azure, for example.)

Anything that needs to be done either in Azure or AAD must be done through operations provided by the shared `Marain.Instance` code. It passes in an object that provides various methods that provide the necessary services.

## Consequences

The amount of deployment code required in individual services is drastically reduced. What remains expresses the particular requirements of the service in question.

The main downside is that if a service has unusual requirements, `Marain.Instance` needs to be modified to make the necessary new capability available.