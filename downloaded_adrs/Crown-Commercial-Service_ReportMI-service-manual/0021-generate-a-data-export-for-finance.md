# 21. Generate a data export for finance

Date: 2018-08-29

## Status

Accepted

## Context

On a regular basis we need to provide data from Report MI to the CCS finance
system (Coda). This data is used to keep track of spend on frameworks and to
issue invoices for the management charge.

### How this works in MISO

MISO generates a CSV file each night containing submitted data. This file is
then transferred to CCS via SFTP.

The export file is run through an extract, transform, load (ETL) process in the
Data Warehouse to fix formatting and several known problems with the export, and
is then passed to the finance team who import it into Coda.

Following the import, invoices are generated and sent to suppliers for payment
of the management charge for the framework.

### Future of Coda

The Coda system is being replaced with Workday. Coda is expected to be switched
off in April 2019 (at the start of the new financial year), with a period of
dual running before hand.

Because we will be taking real submissions before April 2019, we will need to
integrate with both Coda and Workday to ensure that CCS can continue to collect
the management fee.

### Exported data

Coda doesn't require a complete export of all the submitted data - instead, it
needs aggregated sales totals for suppliers, frameworks and sectors.

Coda requires the following fields:

Field | Description |
----------|----------
Run ID | ID of the submission to assist with debugging and audit
Nominal | ID of the framework (or part of framework)
Customer Code | ID of the supplier
Customer Name | Name of the supplier (truncated to 30 characters)
Contract ID | Name of the framework (the RM number)
Order Number | Reference provided by supplier
Lot Description | Description of the Lot/Tier used
Inf Sales | Value of sales (invoices) provided
Commission | Value of the management fee to be charged
Commission % | Rate of the management fee
End User | CG (Central Government) or WPS (Wider Public Sector)
Submitter | Name of the user who has submitted the data
Month | Month that this submission belongs to
M_Q | Whether this should be billed monthly (M) or quarterly (Q)

### The export in Report MI

In [ADR-0002][adr-0002] we outlined the overall technical approach for the
service, and highlighted the components which we expect will be developed.

In that ADR, we suggested that the data exports (including the finance export)
would be standalone components within the overall system.

After discussion with the team, we believe the correct approach for the Coda
export is to generate it as a report in Ruby using the API application. This
will reduce the effort required to generate a separate component for a service
that will be decommissioned in a few months time.

## Decision

We will generate a CSV file on a regular basis containing the fields listed
above.

The CSV file will be stored in an S3 bucket (as outlined in
[ADR-0013][adr-0013]).

The file will then be transferred to the finance team to be loaded into Coda.
The method of transfer will be defined at a later date.

The code to generate the CSV file will live in the API application rather than
a standalone component within the system.

This export will be removed once Coda is decommissioned in April 2019. A
replacement integration for Workday will be developed to replace this.

## Consequences

We will alter the API application to generate the required CSV file.

We will generate the file on a regular basis and transfer it to the finance
team. The regularity of generation and the transfer mechanism will be decided
later.

We will remove this code after Coda has been decommissioned.

[adr-0002]: 0002-overall-technical-approach.md
[adr-0013]: 0013-use-s3-for-storing-files.md
