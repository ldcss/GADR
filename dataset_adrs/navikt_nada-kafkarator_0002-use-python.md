# 2. Use Python

Date: 2020-02-25

## Status

Accepted

## Context

Many k8s operators use Golang, but none of us working on this project are proficient with Golang.
Another option was Rust, which could be a useful learning exercise.
Python is used in FIAAS, so we have some experience using it for an operator.

## Decision

We will use Python for Kafkarator.

## Consequences

Using Python will get us up and running quickly, leaning on experience from FIAAS.
Some team members are less used to Python, so requires some work to get up to speed.

