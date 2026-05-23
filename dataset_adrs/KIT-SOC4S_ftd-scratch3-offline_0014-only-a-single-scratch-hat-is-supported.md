# 14. Only a single scratch hat is supported

Date: 2019-10-20

## Status

Accepted

## Context

Scratch can run many hats at the same time.  
This could be implemented on the arduino using cooperative multi-threading.  
However this would be non trivial to get right.  
The ftduino library has not been built with multi-threading in mind as hasn't the Arduino standard library.  
Also program space is limited and more complex programs already take up most of the memory.  
Adding a user mode scheduler and everything that is needed for cooperative multi-threading will likely exhaust the available memory.  

## Decision

We will only support a single scratch hat, i.e., multi-threading will not be supported.  

## Consequences

Multi-threading becomes impossible.  
Not all scratch programs can be converted for the arduino.
