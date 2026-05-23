# 4. Structure for Terraform projects

Date: 2017-05-25

## Status

Accepted

## Context

We wanted to agree on our Terraform code organisation to manage resources in different stacks and
avoid having to recreate things every time we refactor code.

## Decision

- We want to separate code from data, so in the future we can opensource the code without disclosing our implementation details
- We want to be able to encrypt sensitive data in the repository: we want to support sensitive data encryption as part of the same
process, without having to manage secrets in a different repository, with different scripts, etc.
- We want to create Terraform modules to reuse code
- We want to separate Terraform code into different projects (stacks, tiers), each one representing a logical tier. This is specially
important to separate resources between GOV.UK applications.

The initial solution presents three directories: data, modules and projects:
- The data directory contains a subdirectory per Terraform project, to store variable values that can be customised per environment.
- The data directory also contains \_secrets files with sensitive data encrypted with 'sops'
- The modules directory contains a subdirectory per Terraform provider
- The projects directory contains the Terraform stacks/tiers

```
├── data
│   ├── gke-base
│   │   ├── common.tfvars
│   │   └── integration.tfvars
│   ├── gke-cluster
│   │   ├── common.tfvars
│   │   └── integration.tfvars
│   └── my-application
│       ├── common.tfvars
│       ├── integration.tfvars
│       └── integration_secrets.json
├── modules
│   └── google
│       ├── container_cluster
│       │   ├── main.tf
│       │   └── variables.tf
│       ├── dns_managed_zone
│       │   └── main.tf
│       ├── mysql_database_instance
│       │   ├── mysql.tf
│       │   └── variables.tf
│       └── network
│           ├── network.tf
│           └── public_subnetwork
│               └── main.tf
└── projects
    ├── gke-base
    │   ├── integration.backend
    │   ├── main.tf
    │   └── variables.tf
    ├── gke-cluster
    │   ├── integration.backend
    │   ├── main.tf
    │   └── variables.tf
    └── my-application
        ├── integration.backend
        ├── main.tf
        └── variables.tf
```

## Consequences

The current secrets management solution implicates that we have to decrypt the secrets files at run time and
make sure we clean up unencrypted files after running the Terraform commands.

There are some parameters that are going to be common to different stacks, for instance, 'zone_name'. At the
moment we are going to configure this parameter wherever it's needed, which is different to the behaviour of
Hiera, where we can reference the same parameter in several parts of the code.
