# 6. Create Reference Implementation Repository

Date: 2019-01-14

## Status

Accepted

## Context

The rig defined at [Bookit Infrastructure](https://github.com/buildit/bookit-infrastructure) is an instance of the AWS Bare Metal Rig.  
Whilst it's rather generic as it is, it is specific to Bookit's needs.  
The AWS Bare Metal Rig is also intended to offer choices for the different components (Compute - ECS EC2 vs ECS Fargate vs EKS, RDS - Aurora MySQL vs Aurora Postgres vs Aurora Serverless, etc).  
The only way to capture that is via branches which can be hard to discover.  
Finally, there is not a single repo that represents the latest and greatest version of the AWS Bare Metal Rig.  As instances of Rigs diverge, it is difficult to instantiate a new one that includes all of the latest features

## Decision

Create a digitalrig-metal-aws repo (https://github.com/buildit/digitalrig-metal-aws) that demonstrates all of the options and latest features of the AWS Bare Metal Rig and removes any Bookit specific wording/concepts.

## Consequences

Projects looking to instantiate new AWS Bare Metal Rigs shall be able to clone this reference implementation, make choices nad changes specific to that project, and instantiate their project specific Rig.
Changes and enhancements will need to be implemented in 2 places:  1) the project specific Rig and 2) the AWS Bare Metal reference implementation Rig so that future implementations will contain the latest features
