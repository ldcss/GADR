# 7. Use service specific contact details

Date: 2019-10-11

## Status

Accepted

## Context

The search index contains two sets of contact details, one for the
organisations and one for the psychological therapies services provided by the
organisations. The service contact details are usually more specific, e.g. a
direct telephone number rather than the hospital switchboard, so likely to be
more useful to someone searching for a psychological therapies service.

## Decision

Use the service specific contact details stored as metrics instead of the
organisation contact details in the Contacts field.

## Consequences

Contact details presented likely to be different for the majority of service
providers, but also likely to be more relevant.
