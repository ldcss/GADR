# 5. Configuring DLXS

Date: 2021-01-28

## Status

Proposed

## Context

DLXS has machinery to assemble an XSLT template via a path fallback mechanism.

Because the uplift will not be immediately applied across all collections, DLXS will need to be extended to support an alternative assembly process.

## Decision

Update DLXS:

* Configure a `collmgr` setting to flag a collection as being "uplifted"

* If detected, the fallback machinery will look in an uplift-specific path fallback to avoid any existing XSLT templates

## Consequences

Hacking DLXS; what could go wrong?