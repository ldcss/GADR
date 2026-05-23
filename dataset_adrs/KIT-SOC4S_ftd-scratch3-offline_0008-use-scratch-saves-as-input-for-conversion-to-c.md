# 8. Use scratch saves as input for conversion to C

Date: 2019-10-20

## Status

Accepted

Amended by [19. Allow direct input of project.json without a .sb3 file](0019-allow-direct-input-of-project-json-without-a-sb3-file.md)

## Context

We need a way to get the used scratch blocks from a scratch program.  
We could directly use the format scratch internally (when running in the browser) uses to represent the program.  
This would mean that more code would have to be written in Javascript to interface with scratch.  
This would also couple us tightly to the internal representation scratch uses.  
We could use the format scratch uses to save the program.  
Its format is defined [here](https://en.scratch-wiki.info/wiki/Scratch_File_Format) and it is stable for scratch3.  
Using the scratch saves as input is also more flexible than using an internal representation.  

## Decision

We will use scratch's .sb3 save files as input.

## Consequences

-
