# ADR 1: Authentication Driver Source Type

Tylor Steinberger <tsteinberger@sparks.network>,
Frederik Krautwald <fkrautwald@sparks.network>

## Status

~~Proposed~~ | **Accepted** | ~~Depreciated~~ | ~~Superceded~~

## Context

The Authentication Driver needs to represent multiple outcomes according to the
response types that are returned by firebase to the client. Deciding what data
structure should be used to represent this, we see the following options:

1. Standardize on the `firebase.UserCredential` type by enforcing errors to
adhere to the `firebase.UserCredential` interface. This would be okay because
it would acheive a single type to develop logic against. This may not be okay
because it might misrepresent Errors and make difficulty in distinguishing
the differences between Errors and UserCredentials. This misrepresentation can
make it harder to communicate the intent to future developers.

2. Return either a `firebase.UserCredential` *or* an Error type. This may be okay
because it would have a clear separation of Errors and UserCredentials. This may
be not okay because it forces the client to handle multiple types, and can become
much harder if later combined with other types.

3. Return a new type that represents *both* Errors and UserCredentials. This may
be okay because it allows simple checks for what the type is representing. This
may not be okay because it still requires the client to check for the different
representation of types.

4. Create a common Interface between Errors and UserCredentials that is implemented
to represent both types. This may be okay because it allows the client to work
with a common interface and allows for a minimal amount of checks. This may not
be okay because it introduces a larger codebase that is written using the keyword
`class` and object-oriented programming (OOP) techniques which may not be familiar to
all developers, and may require the use of try and catch loops that can be
negative for performance as current generations of JavaScript engines can not
optimize them.

## Decision

We will return a new type that represents *both* Errors and UserCredentials.

## Consequences

We require a minimal amount of control statements.

We are able to implement this solution relatively quick.

We are able to program against a single interface.

We will have to introduce additional control statements.

We are able to avoid using the keyword `class`.

We are able to avoid deoptimizing try and catch loops.