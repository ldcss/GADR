# 3. Extract scripts from Dockerfile RUN steps

Date: 2018-02-05

## Status

Accepted

## Context

Dockerfiles make no provision for extracting duplication of steps unless they are rendered from a template. Similar `RUN` steps can multiply across different files.

`RUN` steps also allow no logic or encapsulation, and promote long chains of commands due to the necessity of producing a single layer.

`RUN` steps are not testable in isolation or re-runnable inside an image for debugging.

## Decision

Extract long `RUN` steps (or sequences of steps) into a bash script. If the script is only to be used by `root`, place it in `/root/scripts`.

## Consequences

Dockerfiles should not grow to more than 10-20 lines, or at least not because of `RUN` steps.

Every time a single script is modified, the `COPY scripts/ ...` step will be invalidate and re-executed.
