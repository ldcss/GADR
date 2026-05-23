# 40. HPA

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

Implements [39. Least privilege access](0039-least-privilege-access.md)

## Context

High privilege access (HPA) limits production access for developers to only the components and period this access is required to investigate issues of check system health. This implements the [principle of least privilege](0039-least-privilege-access.md) for support on production systems.

## Decision

We will use a high privilege access procedure to secure access to production systems for support.

## Consequences

HPA reduces risk for systems protected by it. However, it introduces additional overhead introduces delay in solving problems. The right level of automation can reduce this delay to an acceptable level.
