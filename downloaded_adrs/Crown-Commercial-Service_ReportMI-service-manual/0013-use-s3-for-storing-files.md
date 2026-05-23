# 13. Use AWS S3 for storing files

Date: 2018-07-18

## Status

Accepted

## Context

The Data Submission Service will need to store various files both during and
after the submission process.

1. **Submission files** - the service will be receiving uploaded files from
suppliers each month. These files will need to be stored somewhere prior to
processing, and will need to be retained for audit purposes for a period of time
afterwards.
1. **Finance export files** - the service will be producing a daily set of files
to be transferred to the CCS finance system (Coda) to allow it to generate
invoices
1. **Data Warehouse export files** - the service will be producing a daily set
of files to be transferred to the CCS Data Warehouse to allow the MI team to
perform analysis of the data.

In [ADR-0008][adr-0008] we decided to use Amazon Web Services (AWS) for hosting
the service. AWS offers object storage for this use-case: AWS [Simple Storage
Service][service-s3] (S3).


## Decision

We will store submission and export files in AWS S3.

## Consequences

We will configure the S3 buckets using Terraform as outlined in
[ADR-0006][adr-0006].

We will need to be careful with the configuration of the S3 buckets to avoid
accidental leakage of data. AWS provides useful tools to check that buckets
are not publicly accessible.

[adr-0006]: 0006-use-terraform-to-create-and-document-infrastructure.md
[adr-0008]: 0008-use-aws-for-hosting.md
[service-s3]: https://aws.amazon.com/s3
