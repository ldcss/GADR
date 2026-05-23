# 3. use terraform enterprise for backend

Date: 2019-11-12

## Status

Accepted

## Context

Terraform writes plaintext of the state of our backend. The ability to collaborate in the workspaces is severely handicapped by this. Many groups use AWS and/or GC storage with dynamodb locking on the state of the file to avoid clobbering on each other. Using Terraform Cloud for small teams will allow us a little more leeway and one less thing to manage. 

## Decision

Use Terraform Cloud for teams

## Consequences

We are trusting Hashicorp to do right by us.
