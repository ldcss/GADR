# Invalid address over missing exit instruction


## Context

We want programs to always terminate with an explicit exit system call, instead of automatically exit with status 0 when the execution reaches the last program instruction, for better consistency and transparency.

In the current version of the Processor, we use unbounded Address values: this prevents us from recognizing that the program misses an exit instruction, because we will theoretically be able to increment the Address indefinitely. This is in contrast with the case where the Processor was reading directly from the Memory, that by definition had a limited size, so that when the Program tried to read an Address that was outside of the memory, it was the signal the the exit instruction was missing.


## Decision

We will let the Program throw an Invalid Address exception when the given Address cannot be found in the Program. This will happen both when a jump instruction tries to jump to an invalid address, and when the execution reaches the end of the Program with no exit instruction having been provided, at which point the next address will naturally not be valid.


## Status

Proposed


## Consequences

It won't be possible for the Processor to tell if the given Program is specifically missing an exit instruction, because that would look exactly like an invalid jump instruction. We accept this situation under the assumption that programs won't usually be written directly in hexadecimal, but using a compiler or at least an assembler, that can be designed to signal the absence of the required exit instruction.
