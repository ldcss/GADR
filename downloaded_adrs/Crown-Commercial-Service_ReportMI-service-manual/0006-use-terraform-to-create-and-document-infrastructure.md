# 6. Use Terraform to create and document infrastructure

Date: 2018-06-07

## Status

Accepted

## Context

Running a service like the Data Submission Service requires infrastructure of
various kinds.

It's good practice to manage this infrastructure using code (Infrastructure as
Code), as this allows the infrastructure to be version-controlled and managed
like the rest of the application code.

There are various mechanisms for doing this. Each of the main cloud providers
have their own solutions to manage infrastructure in code, for example Amazon
Web Services (AWS) has CloudFormation, Microsoft Azure has Resource Manager etc.

However each of these are specific to the individual cloud provider.

It would also be possible to do this manually by running scripts against the
cloud provider API. However, this would take a significant amount of time and
would take effort to make it work across more than one cloud provider.

There are tools available, like Terraform, which allow you to define
infrastructure as code, in a standard way which can then be applied against more
than one cloud provider. The tool handles the differences between providers.

## Decision

We will use Terraform to create the infrastructure for the Data Submission
Service.

## Consequences

We will store Terraform scripts in GitHub alongside the application code.
