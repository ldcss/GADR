# Operating System Patching

Date: 02/10/2019

## Context

Any operating systems that we use are likely to be patched for bug-fixes or security reasons at least once per month. Ideally we would pick up the latest stable release all the time, however this implies a great deal of churn. Such change would also come in spikes of activity e.g. around Windows patch tuesdays.

## Decision

We will not patch our operating systems in AWS. Instead we will pin every instance to a specific version of an operating system and move the pin (via a PR) only when necessary.

## Consequences

We are likely to fall behind the latest version of every operating system and must accept the risk of doing so. We will do the absolute minimum of testing against a specific version of operating system, however any testing that we do complete is derisked by the fact that we have a well-understood mechanism for moving OS versions on a per-environment basis i.e. by moving a pin for one environment at a time.
