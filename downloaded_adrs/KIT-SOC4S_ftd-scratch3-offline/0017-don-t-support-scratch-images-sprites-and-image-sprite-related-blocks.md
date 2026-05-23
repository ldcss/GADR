# 17. Don't support scratch images/sprites and image/sprite related blocks

Date: 2019-10-20

## Status

Accepted

## Context

Scratch supports images/sprites.  
The ftduino has no way to show images/sprites.

## Decision

Scratch images/sprites and image/sprite related blocks are not supported.  

## Consequences

Images/sprites and image/sprite related blocks can not be used. Converting these blocks to C will fail.
