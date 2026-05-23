[<-previous](0006-store-built-documentation-in-branch.md) | [next->](0008-pace-syntax-guiding-principles.md)

# 7. Developer scripts storage location

Date: 2020-Jul-15

## Status

Proposed


## Context

When developing new algorithms and features for PACE-related software,
developers often create useful demo/visualisation scripts for their own use.
These scripts could be useful or interesting for other developers, and are
important for reproducibility or justifying design decisions. They should be
stored somewhere in version control so that they can be easily accessed by any
developers and referred to later. However, they are not intended for general
use and will not be actively maintained or tested. There are 2 main options:

* Store them in a `dev_scripts` directory in each separate project repository
* Store them in a `scripts` directory in `pace-developers`

If they're in the `dev_scripts` directory for each project repository:
+ All in one place
+ Scripts will be close to the code they are used for
- Scripts may not work with the version of the code they are distributed with
- It's unclear where scripts that use more than one project would go
- Despite the folder being called `dev_scripts` people might expect the scripts
to actually work as they're in the main project repository

If they're in a `scripts` directory in `pace-developers`:
+ They can be kept close to the decision-making developer documentation that
they support
+ A version can be specified for any project dependencies

## Decision

Developer scripts will be stored in an appropriately placed `scripts`
directory in the `pace-developers` repository. Depending on whether the
script is tied to a particular software, or general algorithm development
it could be stored in `pace-developers/euphonic/scripts` or
`pace-developers/powder_averaging/scripts` for example.


## Consequences

* Scripts that are intended for development only should not be committed to
the master branch of main software repositories
* Any development scripts committed to `pace-developers` should specify the
exact version of any software they have been developed against. This should
be in the form:
  - `vrelease.version` if if they have been developed against a release
    version of the software
  -  `vrelease.version+ncommits.commithash` (e.g. `v0.11+5.g1076c97`) if the
     project uses
     [versioneer](https://github.com/warner/python-versioneer)
  - `vrelease.version+commithash` (e.g. `v0.11+g1076c97`) if the project does
    not use versioneer (to avoid having to manually count the number of
    commits since the last release)
