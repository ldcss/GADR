# 1. HTTPS implementation

Date: 2018-06-25

## Status

Accepted

## Context

We needed to implement HTTPS and TLS termination as part of the template we offer in our MVP.

We identified 4 ways to get that done.


### Technique #1 - using existing nginx inside the Jenkins container

Our Jenkins master container has nginx installed in it. We can install the certificates and keys
there. That is probably the simplest solution without the need of introducing other
infrastructure components. Also, that allows us to benefit from having an EIP, which is
static, so it could be used for IP whitelisting, if necessary.
 
However, the installation and renewal of certificates has to be done manually, which is a major downside.


### Technique #2 - using ELB

We introduce an ELB in front of the existing infrastructure, like so:

DNS resolution -> ELB -> Jenkins master EC2

Compared to #1, the major benefit is the ability to manage the provisioning of the certificate fully within AWS using [AWS Certificate Manager](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-server-cert.html).

The downsides is not having an EIP (for whitelisting) and that automatic renewal of the certificate meaning higher operational overhead.


	
### Technique #3 - using ELB with ASG

This is like Technique #2 but we introduce an ASG (auto-scaling group) for the EC2 master instance.

By using ACM, ELB and ASG together, it allows AWS to manage the certificate provisioning and renewal, thus removing any operational overhead.



### Technique #4 - using a NLB

Like #2 but with a Network Load Balancer (NLB), like so:

DNS resolution -> EIP -> NLB -> ELB -> Jenkins master EC2

The advantage is that we can have an EIP. However, we probably need Cloudwatch
to detect changes in the EIP which would trigger a Lambda to register the new EIP with the NLB, this is a suggested solution from AWS, but the downsides is that it is complex, expensive and difficult to manage.


## Decision

After exploring and understanding all of the techniques and discussion within the team, option 3 was chosen. 
We draw upon experience of the solution from others within GDS who had successfully implemented it in the past. 
We also liked that it reduces the operational overhead of managing certificates completely.
We were concerned that since does not offer static IPs (via EIP) but we decided that they were not necessary for the MVP as they had not been identified as important during our user research sessions.


## Consequences

Our MVP supports HTTPS without the need to manually issue a certificate, which keeps the provisioning of our
Jenkins simple and quick.

As a consequence of implementing #3 we have to provision the system in a non-UK region, this introduced data sovereignty concerns. The need to use a non-UK region is because some AWS services (EFS) are not yet available in the UK.
