# Help Handlers

## Status

proposed

## Context

How is the responsibility for providing help context defined. 

## Decision

All handlers defined for slash commands are responsible for exporting
a 'handlerHelp' function that will be callable with the string[] supplied
by the help handler. This delegates the responsibility for help to the
author of the slash command handler and co-locates the help definition
with the handler it self. 

## Consequences

This keeps the help handler from being crowded with details and logic
subject to change as code in the other handlers evolve. The down side
is it does decentralize the syntax and style used in help which may
lead to troubling inconsistencies over time. This should be addressed
in code reviews.