# 23. Workday integration principles

Date: 2018-10-10

## Status

Accepted

## Context

As described in [ADR-0021][adr-0021], Report MI needs to provide a regular feed
of data to the CCS finance system. This feed is used to keep track of spend on
frameworks, update the General Ledger and to issue invoices for the management
charge.

Currently, this is done by generating a CSV export which is then be imported
into the existing Coda system.

Coda will be replaced with Workday in April 2019. This means we need to change
how this data feed works.

Following a joint workshop between the Workday and Report MI teams, we have
agreed the following principles to describe how the integration will operate.

### Integration principles

1. **Use APIs** - all communication between Report MI and Workday will be via
APIs. We will not use files to transfer data.

1. **Use common identifiers** - we will use a common identifier for suppliers
and frameworks. We will use the Salesforce ID of the supplier and the RM
reference number of the commercial agreement as our identifiers.

1. **Use common data** - Workday will not source supplier or framework
information from Report MI. Report MI will not source this data from Workday.
Both systems will treat Salesforce as the source of truth for this information.

### Process principles

1. Report MI will create **draft** invoices in Workday as soon as a submission
is approved

1. Report MI will create one invoice per supplier per commercial agreement.

1. Invoices created by Report MI will have an individual line item for each
sector and each management fee as appropriate. For example, they will have
separate items for Central Government and Wider Public Sector spend. There will
be separate line items for the CCS management fee and the Government
Communication Service Fee.

1. Where the total value of an invoice (taking account of all sectors,
management fee types, reductions and refunds) is negative, Report MI will create
a Credit Note rather than an Invoice.

1. With each invoice, we will store metadata including Report MI Submission ID,
RM number, Sector and Sales value. Workday will use this metadata to
automatically update the General Ledger as appropriate.

1. If the creation of the invoice fails because either the commercial agreement
or supplier does not exist in Workday, Report MI will retry at regular intervals
and after a defined time period, report a failure for investigation.

1. Report MI will report the generated invoice number and status back to
suppliers.

## Decision

We will follow these principles when designing and building the integration with Workday.

## Consequences

We will use an API to integrate with Workday.

There will need to be a process through which suppliers are set up in Workday. This process falls outside of the relationship between Report MI and Workday, and has been discussed separately.

Workday will need to store the Salesforce ID against suppliers (this has already been planned for by the Workday team)

There will be finance process changes as a result of these principles (eg stopping manual file processing, and decisions around how invoices are sent / consolidated). These changes are entirely within the responsibility of the Finance team and Workday project.

[adr-0021]: 0021-generate-a-data-export-for-finance.md
