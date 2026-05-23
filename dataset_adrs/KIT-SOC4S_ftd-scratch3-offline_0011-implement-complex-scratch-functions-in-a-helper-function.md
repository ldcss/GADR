# 11. Implement complex scratch functions in a helper function

Date: 2019-10-20

## Status

Accepted

## Context

Some scratch/ftduino functions take complex arguments that need to be verified.  
Some scratch/ftduino functions are complex to implement.  
The code for these functions could be directly generated in the java files for the specific function.  
The code for these functions could also be written inside a helper function, such that only a single line - that calls the helper function - is generated for such a function.  
Writing these functions in a helper function also makes changes and code reuse easier.  

## Decision

Complex scratch/ftduino functions will be implemented in helper functions and those will be called by the generated code.

## Consequences

Helper functions can be easier reused and changes have to only happen in one place.   
