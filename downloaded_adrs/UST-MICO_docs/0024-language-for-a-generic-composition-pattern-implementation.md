# Language for a generic composition pattern implementation


## Context and Problem Statement
We need to decide which language to use for implementing a MICO composition service. 
The framework will be [Apache Kafka](https://kafka.apache.org) [See ADR0021](0021-kafka-as-messaging-middleware.md) 

## Decision Drivers 

* Should be known by everyone (on the developement team)
* Must support Apache Kafka

## Considered Options

### Java 
Pro: 
* Easy setup with [Spring boot](https://spring.io/projects/spring-kafka)
* Java is the only language in which every team member is proficient in

### Python
Python was only used in the prototyping stage and was not explored further

## Decision Outcome

We want to use Java. Since existing knowledge and experience is given for everyone.

