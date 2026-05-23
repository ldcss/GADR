# 2. feat_create_staging_branch

Date: 2020-02-17

## Status

Accepted

## Context

Sometimes while creating something new, code is written to research a 
 possible solution, but later you could find a better way or a different 
 approach to the solution.

## Decision

To avoid messing the master branch with imprudent commits, I'm going to 
 create a _new default branch_, called **staging**.  This way, all the pull 
 requests will be sent to the new branch after merged.  Then, if after
 the pull request is found to have issues, I will be able to fix it 
 without problems.


## Consequences

The good thing is that commit history will be more readable, and more 
 sustainable.  The cons may be it's more work to do, but it worths the
 effort.

