# 16. Don't support scratch sounds and sound related blocks

Date: 2019-10-20

## Status

Accepted

## Context

Scratch supports sounds.  
The ftduino has no way to play sound.  

## Decision

Scratch sounds and sound related blocks are not supported.  

## Consequences

Sounds and sound related blocks can not be used. Converting these blocks to C will fail.
