[<-previous](0004-pace-documentation-link-to-projects.md) | [next->](0006-store-built-documentation-in-branch.md)

# 5. PACE Projects must be semantically versioned

Date: 2020-Jun-20

## Status

Accepted

## Context

The PACE projects will evolve over time and breaking changes will be introduced. Users will need to be able to easily finding the correct documentation for their build.

[Semantic versioning](https://semver.org/) defines a schema in which releases are given `major.minor.patch` version numbers where increments are made to the:
- `major` version with incompatible API changes,
- `minor` version when functionality is added in a backwards compatible manner, and
- `patch` version for backwards compatible bug fixes.

Sphinx plugins are available that support multiple documentation versions ([sphinx-multiversion](https://pypi.org/project/sphinx-multiversion/)) - this will not work correctly for Brille where documentation is extracted from the build artifacts.

## Decision

Projects will be semantically versioned and documentation will be retained and be available for users to access for each major or minor version released. 

There is no requirement to have patch-release specific documentation. 

## Consequences

- Identification of breaking changes and extensions to the API requiring revised documentation will be easy for developers and users to identify

