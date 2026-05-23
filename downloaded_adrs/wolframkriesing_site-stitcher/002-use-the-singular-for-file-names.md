# 2. Use the Singular for File Names

## Status

Accepted

## Context

I have written and seen a lot of code where it was not clear what rules apply, where to find a certain
file, how to write the import correctly is it "render-page.js" or "render-pages.js" 
and bugs caused by those missing definitions. IDE support and types have definitely improved that over the
years. Still I struggle from time to time.

I just renamed a file from "tidbit/render-pages.js" to "tidbit/render-page.js" (the new name is **singular**) 
even though this file contains multiple page-render functions. But if I will start naming a file
depending of how many page-render functions it contains I will have more work renaming when functionality
evolves and will introduce bugs
(I know I have tests to prevent that, but they are not almighty either). I want one way to do it.

For files I want one rule how they are named. That rule applies always and esp. in doubt.

## Decision

**Use the singular for file names** for as much consistency as possible.
As usual really good reasons for exceptions exist, but ask yourself many times if the exception is
worth dropping consistency for.

## Consequences

- it might feel cumbersome in the beginning
+ consistency
+ no time needed to search, just know names