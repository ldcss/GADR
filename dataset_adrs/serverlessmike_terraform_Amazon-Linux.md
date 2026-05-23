# Amazon Linux is Preferred

Date: 02/10/2019

## Context

We are migrating from several different versions of Windows and Linux in DXC to AWS. The easiest migration path would be to move applications and databases to exactly the same platform in AWS. The lowest TCO for the target solution would be provided by migrating onto a small number of consolidated Linux platforms (assuming we can't go serverless for everything). These two options are mutually exclusive, so we need a decision on the way forward.

## Decision

Our strong preference is to go serverless. Where we can't go serverless we prefer to use the latest AWS Linux, but accept that the choice of OS is often dictated by the application and/or database layers.

## Consequences

 - There will be fewer VMs to support in AWS with fewer operating systems variants.
 - There is likely to be a gradual drift from Windows Server to Linux, but it is difficult to say if or when we will no longer require Windows Server images or skills.
 - It is noted that containerisation of applications will help us to protect application from each other and from OS variations, but does *not* completely obfuscate the choice of platform.
