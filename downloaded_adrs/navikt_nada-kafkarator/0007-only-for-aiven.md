# 7. Only for Aiven

Date: 2020-05-05

## Status

Accepted

## Context

NAV currently has Kafka running on-premise, but have plans to move everything to the cloud.

Kafkarator will create an integration between applications and Kafka, removing some manual work and putting more configuration in code.

The plan is to buy hosted Kafka from Aiven, eliminating the need for maintaining our own Kafka cluster on-premise.

## Decision

Kafkarator will only deal with the future solution using Aiven, and not work for on-premise Kafka.

## Consequences

Kafkarator will not be useful for anyone until we have a deal with Aiven in place, and started using it.
Kafkarator will be an incentive for application developers to move to Aiven, as it will hopefully provide benefits that will not be available in the on-premise Kafka.

