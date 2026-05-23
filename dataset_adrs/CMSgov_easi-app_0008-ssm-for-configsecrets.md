# Use AWS SSM Parameter Store for Config/Secrets management

The EASi application
will require configuration for different
environments it is deployed to. These values
may contain secrets. We would like to pick a
set of tools to allow us to securely manage configuration
and integrates easily into our existing toolchain.

In this ADR,
we'll decide what tools we will use
to store configuration and secrets
to enable environment level configuration
to the EASi application.

## Considered Alternatives

* *AWS Secrets Manager*
* *AWS SSM Parameter Store*
* *AWS SSM Parameter Store + Chamber*
* *Hashicorp Vault*

## Decision Outcome

Chosen Alternative: *AWS SSM Parameter store + Chamber*

AWS SSM Parameter store has the features we need
and directly integrates with AWS Fargate. The centralized
access management through IAM and auditing through
Cloudtrail make this a good choice.

Chamber just makes the developer experience a bit
nicer when working with Parameter Store and will make
management of secrets and config a bit easier.

## Pros and Cons of the Alternatives

### *AWS Secrets Manager*

* `+` Automated rotation of secrets
* `+` Auditable through Cloudtrail
* `+` Centralized place to store secrets
* `-` Specifically designed for secrets and config probably  
doesn't need to be encrypted.
* `-` Not commonly used and we do not have experience with it

### *AWS SSM Parameter Store*

* `+` Directly integrates with Fargate
* `+` Auditable through Cloudtrail
* `+` Centralized place to store secrets
* `+` Granular access can be defined in IAM
* `+` Can store config in plain text and encrypt secrets with KMS
* `+` Truss has used this tool before
* `-` A little annoying to manage through AWS CLI

### *AWS SSM Parameter Store with Chamber*

* `+` Directly integrates with Fargate
* `+` Auditable through Cloudtrail
* `+` Centralized place to store secrets
* `+` Granular access can be defined in IAM
* `+` Can store config in plain text and encrypt secrets with KMS
* `+` Truss has used this set of tools before
* `+` Simpler command line management of Parameter store
* `-` Additional setup and tooling to use Chamber

### *Hashicorp Vault*

* `+` Auditable access
* `+` Auto rotates secrets
* `+` Granular access controls
* `-` A whole distributed service to manage
* `-` It requires Consul or something else to back it
* `-` Truss does not have experience with this tool
* `-` Does not directly integrate with AWS Fargate
