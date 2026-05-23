# 2. Infrastructure layout

Date: 2019-11-12

## Status

Accepted

## Context

When creating a piece of infrastructure it is implied that this code would be able to be run in several environments. To illustrate this, there are three environments created, dev, uat, and prod. There will be one and only one 
terraform module and each environment will feed it with different parameters to create distinct instances. 

## Decision

The terraform code is made multi environment and multi account through there are better tools to do that with, like terragrunt, which is outside the scope of the PoS. 
The credentials are assumed to be in the credentials file. the author is aware that the are more secure ways of doing this , but as the PoS needs to be easily reproducible the author has chosen to make it easy to use by dropping in the credential files in the home directory. 
The credentials are that of an administrator, there has been no attempt made to create assumed roles as would be done in production systems, as the goal in this case is speed.
## Consequences

It will be possible to create multiple environments, but it will be limited to one account. 
