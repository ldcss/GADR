# Metadata

## Context

Digital objects need to have associated metadata for various use cases (refer to
 the requirements documentation for details). Metadata of these objects can be descriptive, administrative, and structural.
 To avoid "duplication" of descriptive metadata, it is desired that DOS not store descriptive metadata.

## Decision

Descriptive metadata will not be stored by DOS.

## Status

Accepted

## Consequences

Some use cases or features (such as bulk download of objects) that were originally gathered in DOS business analysis Phase 1
may not be fulfilled by DOS. It is possible that further business analysis may need to be done for these use cases and 
to see if any systems are already fulfilling that role in some capacity.