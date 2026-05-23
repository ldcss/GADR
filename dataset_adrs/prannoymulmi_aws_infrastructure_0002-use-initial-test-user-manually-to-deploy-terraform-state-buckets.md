# 2. Use initial test user manually to deploy terraform state buckets

Date: 2020-06-14

## Status

Accepted

## Context

To use terraform one needs to setup s3 bucket and dynamo lock for multi user access which creates the chicken and egg problem, where the bucket and dynamodb resources have to be present first to start managing Infrastructure with terraform.

## Decision

The requried resources would be bootstrapped using a cloudformation stack and this requires a initial admin user which will be deleted right after the creation

## Consequences

A miyture of cloudformation and terrafrom will be created but inreturn the infrasture would be stored as code given this manual step. It is also important to delete the boostrap user to avoid any security pitfall as soon as the resources are created.
