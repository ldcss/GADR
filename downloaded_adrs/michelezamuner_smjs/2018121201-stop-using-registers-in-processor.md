# Stop using registers in processor


## Context

Communication between processor and interpreter must go both ways: the processor needs to pass the interpreter the instruction to execute, and the interpreter is supposed to be able to update the Instruction Pointer (IP), and to tell the processor it the execution needs to stop, and with which exit status.

Currently we are using an intermediate component, registers, partially like how real processors work, containing both the IP and the information about the exit status. However, the communication between the processor and the interpreter is so straightforward that a much simpler solution would be to just use classical call argument, and call return value. Registers could be used as a mediator, but for this to have sense the processor and the interpreter would have to be unaware of each other, and registers should implement a mechanism to automatically notify involved parties when a change is made, which seems overkill.


## Decision

The interpreter will keep taking an instruction from the processor, but this time it will return a data structure, which tells if an exit has been triggered, and in this case what's the exit status.


## Status

Accepted


## Consequences

The processor doesn't need to define an interface for registers, and interpreters don't need to implement it anymore. Communication is simplified.
