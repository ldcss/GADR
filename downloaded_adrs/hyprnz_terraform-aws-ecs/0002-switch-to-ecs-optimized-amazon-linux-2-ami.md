# 2. Switch to ECS-Optimized Amazon Linux 2 AMI

Date: 2018-11-13

## Status

Accepted

## Context

Amazon have introduced a new ECS-Optimized instance based on the new Amazon
Linux 2. This
[ECS-Optimized Amazon Linux
2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/al2ami.html)
instance has also changed the Storage Driver from `devicemapper` to `OverlayFS`.
The old ECS-Optimized instances will be phased out and not supported beyond June
2020.

Storage configuration has also been changed as the [Amazon 2 Storage
Configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/al2ami-storage-config.html)
consists of a single 30GB root disk. The old [Storage
Configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-ami-storage-config.html)
which had a 30GB drive split into 8GB for the OS and 22GB for storage.

## Decision

We will roll out the new ECS-Optimized instances into the environments on a
rolling basis starting with DEV to ensure there are no issues with our current
container workloads with the change in Storage Drivers.

This will also allow us to determine if we need to increase the size of the
storage for use in our Kafka cluster which has specific storage requirements.

## Consequences

We will need to update this module to get the AMI using the Amazon 2 metadata
and then roll the change into the DEV environment and monitor for any issues.

Once we have rolled the changes into DEV we will then need to roll changes
through to the ACCP and PROD environments.
