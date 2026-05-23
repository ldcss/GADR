# 15. Use floats for storing numbers not doubles as scratch does

Date: 2019-10-20

## Status

Accepted

## Context

Scratch uses Javascript's numbers type to store all numbers it uses. The Javascript number type is effectively a 64 bit double.  
The ftduino only supports 32-bit floats.  
64-bit double emulation might be possible but slow and likely exhaust the available memory and program space.    

## Decision

We will use 32-bit floats to store any numbers.

## Consequences

Using 32-bit floats will lead to a loss of range and precision.  