# 3. Deploying metadata to PaaS 

Date: 2018-03-13

## Status

Accepted

## Context

Currently we are migrating stub IDP from UKCloud to PaaS. Stub IDP uses hub metadata to validate signatures 
and to achieve this, we need to whitelist the IPs that needs access to hub metadata. Inorder to whitelist we need  
static IP address for stub IDP in PaaS for certain environments (`joint, integration, staging, perf`). 
This feature is currently not offered by PaaS. 

## Decision

We have decided to deploy hub metadata to PaaS as part of the current metadata release process. 
Whenever metadata is being deployed to UKCloud there is a copy of it being pushed to
PaaS so that both (UKCloud and PaaS) use the same version of metadata.  

## Consequences

This results in duplication of hub metadata but this could be removed once IP whitelisting
is removed from the environments. 
