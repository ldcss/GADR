# We Will Use AWS AMIs Only

Date: 02/10/2019

## Context

We have many operating systems in play at DXC. In moving to AWS the number of potential variants does not decrease, as we could choose from AWS images, marketplace images, or we could build/maintain our own images.

## Decision

We will use AWS images only, as this frees us from the operational overheads of patching and testing. AWS have been the fastest company in the cloud space to patch their operating systems in response to threats, so we can benefit from their good practices. This decision also allows us to take the easiest routes for automation and gives us access to the widest range of public cloud software.

## Consequences

Customisations of operating systems will have to be kept to a minimum and will need to be automated. We cannot specify the latest version of an image, unless rebuilding an instance when running `terraform apply` is desirable.
