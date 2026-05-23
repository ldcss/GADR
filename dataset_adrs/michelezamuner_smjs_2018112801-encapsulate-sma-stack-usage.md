# Encapsulate SMA stack usage


## Context

Real world assembly programming exposes the stack pointer and the base pointer, allowing assembly code to directly mess with them, for example changing the stack pointer regardless of how `push` and `pop` instructions have been used. Despite allowing wild optimizations, this is really error prone and, if used extensively, makes programs very obscure: for these reasons, we don't want to support such things in our SMA architecture.


## Decision

To prevent code from messing up the stack, we'll avoid adding public stack pointer and base pointer registers. Rather, these two concepts will still be used in the implementation of the stack object, but clients won't be able to directly use them, since the only interfaces allowed will be the usual `push` and `pop`, which will take care of properly updating the stack pointer and the base pointer.

Since pointers are not directly usable from the code, we need to add a way to abstract the concept of stack frame: this is the role of the `pushFrame` and `popFrame` methods: the first one takes the return address, and takes care of pushing it on the stack at the right moment, while the second one will return the previously stored return address.

Another problem with encapsulating frame handling, is that of passing procedure arguments to the stack. In regular assembly, one first pushes the arguments, then pushes the return address and the base pointer, and the jumps to the procedure. From inside the procedure, to get the passed arguments it's then necessary to first temporarily pop the base pointer and the return address, then pop the arguments, and then push back return address and base pointer.

Since we don't want to write all this boilerplate every time we call a procedure, we'll provide an alternative `call` instruction, supporting argument passing: this instruction will take the size of the pushed arguments (in bytes), and will automatically move the pushed arguments over the return address and the base pointer, after having pushed these, so that the procedure code will immediately find the arguments at the top of the stack, without the need to do any boilerplate.


## Status

Accepted


## Consequences

Procedures are now very consistent, because their interface always use only the stack, and never the registers (although they're still visible, and thus usable of course): the arguments are found on the stack, and the return value is returned from the stack too.

Of course it's still possible to mess up the stack, for example if someone pops too many things right after the procedure call, he could end up popping the return address and the base pointer off the stack. This probably smells of a design criteria (that of simplifying the usage of the stack) that is being implemented only partially. On the other hand, the main design goal of the project is that of being as close to the implementation of real processors as it makes sense to do so, so this solution is to be intended as a compromise.
