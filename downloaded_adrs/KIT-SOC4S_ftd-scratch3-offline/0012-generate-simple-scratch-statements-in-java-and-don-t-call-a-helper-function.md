# 12. Generate simple scratch statements in java and don't call a helper function

Date: 2019-10-20

## Status

Accepted

## Context

Adr 0011 says that complex scratch functions will be implemented in helper functions.  
For statements like if/else/while this is harder to do.  
An "if" function would have to take a function that is executed on success.  
This would be more complex than simply using a c "if" statement.  

## Decision

The code for simple scratch statements will be directly generated in the java file.  
Simple scratch statements are e.g. if/else/while.  

## Consequences

-