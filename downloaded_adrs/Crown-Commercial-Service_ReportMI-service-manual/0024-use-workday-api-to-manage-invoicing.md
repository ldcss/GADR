# 24. Use Workday API to manage invoicing

Date: 2018-11-07

## Status

Proposed

## Context

As outlined in [ADR-0023][adr-0023], CCS will be migrating their finance system
to Workday in April 2019. As part of this migration, invoices sent to suppliers
for the framework management fees will need to be created there rather in
Coda. This means we need to change the process within Report MI.

The principles set out in ADR-0023 state that we will use APIs for all communication
between Report MI and Workday instead of batch exports and file transfers.

### Workday API

Workday provides an API for third-party systems to insert and add data
to a tenant's system.

There are many parts to the API, but there are two endpoints which are of
particular interest to us for invoicing.

- **Submit_Customer_Invoice** - this endpoint allows the creation (and replacement) of invoices within Workday.
- **Get_Customer_Invoice** - this endpoint returns all the information about an invoicing including it's
state and payment status.

## Decision

Report MI will use the Workday API to create invoices in Workday for the
management fee. Report MI will talk directly to the Workday API, not through
any intermediaries - this will reduce the number of moving parts and potential
failure points.

We will use the `Submit_Customer_Invoice` API endpoint to create a new invoice
for each approved submission. As outlined in 0023, we will create one invoice
per supplier, per commercial agreement, per month.

If necessary, we will use this API endpoint to automatically create negative
invoices (credit notes) and/or issue adjustments as required.

All invoices created will be generated with a state of `Draft`.

The unique identifier of the created invoice will be stored by Report MI for
later use.

We will use the `Get_Customer_Invoice` API endpoint to query the state of an
invoice. We will use this to allow Report MI to show the status of issued
invoices to suppliers.

## Consequences

The Workday team will need to provide API access to the Report MI team to enable
this integration to operate. This will need to include appropriate
pre-production environments to enable integration testing.

Report MI team will need to develop features to handle the submission of
invoices to the API.

[adr-0023]: 0023-workday-integration-principles.md
