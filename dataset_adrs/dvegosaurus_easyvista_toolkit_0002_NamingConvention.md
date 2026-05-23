# Naming Conventions
date : 2019/10/01

## Status
accepted

## Context
We need to make sure that the module will be reusable in a friendly way, functions and parameters names should be easy to guess
and should not conflict with other Non-easyvista related module.

## Decision
In order to fullfill our goal :
- We will only use verb from the powershell's approved list  (get-verb)
- We will prefix all our noun with EZV in uppercase
- We will use easyvista's terminology in our nouns:
    - i.e: a service request or a change request will be both referenced as a request (new-EZVRequest) since 
    this is the same from the API point of view (/requests)
- We will add an *s* to any function returning a list of something

## Consequences
### Pros
- cmdlet will be easier to use
### Cons
- none
