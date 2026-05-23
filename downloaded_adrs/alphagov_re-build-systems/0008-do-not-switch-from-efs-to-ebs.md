# 8. Do not switch from EFS to EBS

Date: 2018-09-07

## Status

Accepted

## Context

To guide our work, we need to decide whether we use AWS’ Elastic File System
(EFS) or Elastic Block Store (EBS) as the cloud storage service for our Jenkins
build. 

The decision is needed as it will impact on the team’s work and may be affected
by wider GDS or Government strategy. 

## Decision

Based on the below pros and cons, we have decided to remain with EFS as the
cloud storage service, until such a time that there is a strategic need to
change. 

Because of the way in which the team has compartmentalised the architecture
of and approach to this Jenkins build, it is eminently possible to move to EBS
at any point. It also means that further development of the system will not make
it more complicated to do so. 

It is for this reason that the decision is not to carry out this work in
anticipation of it being needed, but rather focus on existing required work and
only carry out the work of converting to EBS should the need arise, at which
point that work would need to be prioritised.

## Consequences

### Pros and cons of each approach

**EFS**

Pros:

* You only pay for what you use

Cons:

* AWS does not provide EFS in London yet
* It is more expensive than EBS
* Requires a specific binary (EFS utils) to be compiled
* Uses Network File System (NFS), which has a bad reputation although is not a
problem in the context of this system

**EBS**

Pros:

* Can be used in London
* Cheaper than EFS
* Allows for snapshots to be taken, making it easier to backup than EFS

Cons:

* You need to know (predict) your storage needs 
* An increased overhead for the team to monitor usage and then respin the
infrastructure if more storage is needed
* Only one server can mount an EBS volume at a time
* A technological approach to servers mounting an EBS volume makes respinning
the infrastructure error-prone

### Work required to revert to EBS

* Need to design a process for users to define the EBS volume size and then to
do the resizing (respinning the infrastructure, etc.)
* Requires changes to the Terraform code
* Requires changes to user data
* Requires redocumenting
* Need to add monitoring of storage usage (to inform the need to increase or
decrease the size of the EBS volume)

### Other considerations

* If sovereignty of data (i.e. keeping code and data on UK soil in certain
post-EU-Exit scenarios) is an issue, it may also be worth considering that other
AWS services are global (cannot be regionally specified)
  * It may be that Information Assurance (IA) takes a different stance with those
services, however, as they are perhaps less likely to hold or transport
sensitive data
* Even if the decision is made that all Platform as a Service (PaaS) tenancy
must remain in the UK, our current Jenkins could still ‘push’ to a UK-based
PaaS; however, this would need IA approval, depending on which elements of the
service and build pipeline are considered to be sensitive (and therefore must
remain in the UK). PaaS confirmed on 29/08/2018 that this is currently possible
and there are no intentions to change this
* GOV.UK’s approach to using EBS could negate the technical consideration that
makes respinning the infrastructure prohibitively error-prone
* EFS does not support versioning or snapshots; backups are managed by third
party software. AWS does provide an appliance to assist in backing up EFS,
which is essentially a VM running rsync to a date stamped backup directory on
another EFS instance.

