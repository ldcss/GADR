# Define and manage infrastructure with Terraform

We should define pieces of infrastructure in code so that changes can be
reviewed, audited, and tracked over time. We prefer a declarative format that
can be run idempotently so that it's easier to understand the current state of
infrastructure.

We're assuming we'll be using AWS services.

## Decision Drivers

* Is a standard tool that has a community to support it.
* General experience with the tool.
* Must work on AWS services.

## Considered Options

* Terraform
* CloudFormation

## Decision Outcome

Terraform

## Pros and Cons of the Options

### Terraform

* Good, because it is declarative and idempotent.
* Good, because we have deep experience with this tooling internal at Truss.
* Good, because there is a large community that uses and supports this tool.
* Bad, because state management. (Mitigated by experience using the tool.)

### CloudFormation

* Good, because it supports and is deeply integrated in AWS.
* Good, because it is declarative.
* Bad, because the tooling isn't in our wheelhouse of experience.
* Bad because community support would be poor.
* Bad because it has lagging support to their service features.
