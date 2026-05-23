# 3. packer-as-builder

Date: 2019-11-13

## Status

Accepted

## Context

In AWS the use of AIM images is used to create and customize base line and derived application images from. These can be created with a tool like packer that will take a base image, configure it, and then has a ready to use AIM image ready. 


## Decision

Packer is a multi cloud vendor tool specialized in provision images. It has been decided by the author to use this as a quick prototype example of how to use this in a simple CI/CD example. 


## Consequences

It adds some complication to the test for adding an ancillary system, but it is worth to showcase here,
