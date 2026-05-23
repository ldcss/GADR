# ADR - 0001 Choosing an AWS RDS High Availability Solution

Date: 2020-07-01

## Status

Proposed

## Context

Our Production AWS RDS databases are not configured for high availablity which can support blue-green architectures and reduce risk. There exists a few ways to provide HA on RDS. We cover those in this document with the goal of choosing, among other criteria, an offering that aligns with AWS archtectural best practices.

### Distinguishing between HA and DR:

High Availability (HA) provides a failover solution in the event a database, vpc, or availability zone fails. Disaster Recovery (DR) provides a recovery solution across a geographically separated distance (multi-region) in the event of a disaster that causes an entire data center to fail.

In this ADR, we select an architecture that ensures High Availability and defer Disaster Recovery to a separate ADR.

## Criteria

Choosing the right HA architecture should 1) align with AWS Best Architectural Practices, 2) is cost effective, and 3) minimizes or eliminates disruption to RedLine Production applications using RDS. This measure is commonly referred to as Mean Time to Recovery - MTTR.

## Proposed Solutions

### Use the RDS Multi AZ

Pros:

- Easy to enable using Multi AZ property in AWS RDS Console
- Nothing to port
- Syncronous Replication for instant db consistency at failover (hot standby) and minimal db downtime
- One DNS Name across all standby replicas eliminates application intervention
- 3 levels of failover using Amazon's failover technology: 1)vpc network, 2) db or ebs (disk) crashes, or 3) AZ unavailibility.
- Automatic failover (DNS updates)

Cons:

- DNS cache ttl settings in applications may impact recovery to the failover
- 1 standby availability
- Zero HA when AWS Region fails
- Likely Doubles cost of RDS for each hot replica, and the network traffic to sync data.
- Perhaps some write latency during synchonous writes to standby replicas
- Not a scaling solution

### Use RDS Read Replicas

It is possible to create a failover solution with read replicas, though this is typically done when read replicas have already been deployed into the environment

Pros:

- Move Anayltic or Reporting workloads off of master db on to RR's
- Replicas can be promoted to their own db's in the event the main db fails. This is a manual procedure
- Asyncronous reads create delayed consistencies on replicas but provide zero latency writes to the main db
- Replicas are available within AZ, cross AZ or Cross Region

Cons:
- Failover is manual
- Apps must update connection config
- Read replicas cannot serve db writes and have their own endpoints

### Migrate to Aurora RDS Service

An Aurora cluster is typically used for both scalability and high availability and involves a richer topology and technology than RDS Multi AZ for HA. It is a load balanced service.

Pros:

- Transparent fast failover
- is a highly distributed, high
  throughput database
- Upd to 15 nodes in cluster, master is write, the others are read only
- Can be configured up to 15 replicas
- Failover at all levels Region and under

Cons:

- Application [connection strings](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.html#AuroraPostgreSQL.BestPractices.FastFailover.Configuring.ConnectionString) must be configured for failover
- More to port, more to learn, more to manage
- Amazon claims it is app transparent, but I have my suspicions.

#### Decision

We will apply the RDS Multi AZ architecture to add high availability to our RDS production instances as it is the recommended best practice to adding HA to existing RDS instances.

#### Consequences

- Choosing Aurora DB would be a part of a larger product design decision, outside of this adr scope.
- High Availability for failover protection improves the stability of the product framework. We did not address Disaster Recovery, which should also be a part of an overall scope of the product framework.
- Multi AZ architecture should be fairly transparent to RDS applications, but the failover conditions and alerting mechanisms should be understood prior to implementation.
