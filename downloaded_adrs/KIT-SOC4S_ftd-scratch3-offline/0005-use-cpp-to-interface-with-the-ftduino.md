# 5. Use C++ to interface with the ftduino

Date: 2019-10-20

## Status

Accepted

## Context

The scratch blocks need to be run on the ftduino.  
To run a scratch block a small runtime is needed.  
The ftduino supports both C and C++.  
The Arduino and ftduino library use C++.  
Interfacing from C to C++ is possible but tricky.  
C++ also offers constructs C doesn't e.g. type safe enums.  

## Decision

We will use C++ to interface with the ftduino.

## Consequences

Interfacing with the Arduino and ftduino library is easily possible.  
Writing type safe code is easier.
Some C++ constructs add additional overhead e.g. classes.
