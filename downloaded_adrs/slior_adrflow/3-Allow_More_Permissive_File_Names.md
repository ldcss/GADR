# 3 Allow More Permissive File Names

## Status

Proposed 2017-07-26  
Accepted 2017-07-26

generalized_by [7](7-Defining_Customizations.md)

## Context
Given that the ADR flow tool is intended to be a drop-in tool, and integrate well with other tools and repositories, we should aim also for ADR files created outside the tool, not with the same naming convention.  
The tool generally works with the file system - looking for the ADR dir, enumerating files, etc.

The existing naming convention is rather strict, so the functions looking for files rely on the same regular expression that's used to create it.  
We would like to extend the file enumeration to more options for file names.

## Decision
Change the regular expression that's used to enumerate files to include more options (hypens, spaces).  
File should still be with a `.md` extension, and reside in the ADR dir (the directory identified by `.adr` file).

The file template itself still remains the same.

## Consequences
More file names will be recognized as ADR files.
Functions relying on `withAllADRFiles` will be affected.

    