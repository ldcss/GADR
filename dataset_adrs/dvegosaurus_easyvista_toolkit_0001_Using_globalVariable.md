# Using Global variables
date : 2019/10/01

## Status
accepted

## Context
We want to be able to have autocompletion in the cmdlet to make them more user friendly. 
Because the easyvista rest API relies on GUID for some parameters we'll need to be able to query their friendly name within in the cmdlet parameters.

We tried using environment variables but they don't seem to work with hashtable (we did not check extensively).

## Decision
We will use global variables (named *$Global:EZVvariablename*) set by a dedicated cmdlet (*set-EZVcontext*). That cmdlet will define an execution context for all other cmdlet in the project.

## Consequences
### Pros
- cmdlet will be easier to use
### Cons
- global variable with the same might allready exist.[^1]

[^1]: since this will be used in controlled environment this should not be a big issue.