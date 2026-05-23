[<-previous](0001-record-architecture-decisions.md) | [next->](0003-pace-projects-will-have-independent-documentation.md)

# 2. Use GitHub Pages for user documentation

Date: 2020-Jun-20

## Status

Accepted

## Context

A consistent platform is required for user documentation from the PACE projects: Brille, Euphonic and Horace/Herbert.

Two platforms support, are well used for this service:

- [Read the Docs](https://readthedocs.org/)
- [GitHub pages](https://pages.github.com/)

Both platforms will display documentation built by [Sphinx](https://www.sphinx-doc.org/) from reStructuredText source files.

Brille includes compiled C libraries that contribute APIs to the project. The Read the Docs build/deploy pipeline does not support inclusion of documentation generated from C source.

## Decision

We will use GitHub pages for all PACE project documentation.

## Consequences

- documentation will be available at URLs under `pace-neutrons.github.io` 
- GitHub pages can be configured to make the documentation available at any owned URL
- sources for the documentation are stored alongside the source code
- built documentation is stored in the GitHub
- build pipelines for each project will be required to convert the source `rst` files to `html` for display
- API documentation can be included for compiled C code

