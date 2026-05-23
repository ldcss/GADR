# 19. Allow direct input of project.json without a .sb3 file

Date: 2019-10-27

## Status

Accepted

Amends [8. Use scratch saves as input for conversion to C](0008-use-scratch-saves-as-input-for-conversion-to-c.md)

## Context

We need a way to transfer the scratch save to the local web server.  
Scratch provides a function that serializes the scratch program, but directly returns a json file which would normally be the project.json in a .sb3 file.  
Rather than searching for a method that provides a .sb3 file, we chose to accept the json directly.  

## Decision

project.json can directly be used as input for conversion.

## Consequences

We don't need an .sb3 file anymore.  
This is beneficial because a .sb3 file can also contain images and sounds.  
The current code for handling a .sb3 file will now extract the project.json and use the new code path for json files.
