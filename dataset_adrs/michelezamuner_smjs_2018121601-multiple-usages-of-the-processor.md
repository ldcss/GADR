# Multiple usages of the processor


## Context

The domain our virtual machine is supporting is concerned with running programs: as such, how programs should be run is a business rule, and the Processor is the Domain Service encapsulating that rule.

At the application level, we can think of several features that can support this domain:
- classic virtual machine, running an entire program, perhaps loaded from a file, until its termination
- REPL, where instructions are loaded one at a time from an interactive prompt, and executed, printing some kind of output each time
- debug, where we still have an entire program, but this time we want to support debugging features, like running step-by-step

Of course there could be many others. Can we use the same definition of a Processor in the domain to support all this cases?


## Decision

We will keep the Processor as a Domain Service, because the three different kinds of execution we want to support really only differ for how data is handled in memory, and the domain doesn't concern itself with what is contained in memory (it doesn't even mention memory, since it's a detail of the interpreter, and we might as well use interpreters that don't use any memory):
- in the classic virtual machine, the Program is the entire program, that is executed from start to end
- in the REPL situation, each time a new instruction is inserted at the prompt, it is added to the Program, which is then fed to the Processor: this is necessary because we might have defined procedures that we want to call in the future; the state of memory is saved between different executions (this doesn't concern the domain), and to make the program start at the latest instruction, we add a new unconditional jump instruction at the beginning of it: this actually means that we don't run the entire program again (it isn't necessary since memory is preserved), but only the last inserted instruction
- in the debug situation, the Interpreter implementation can avoid returning control back to the Processor until requested to: this still doesn't concern the Processor implementation in the domain


## Status

Proposed


## Consequences

If the Processor definition in the domain stays abstract enough, only mentioning the real business needs, we can reuse it in different applications situations.
