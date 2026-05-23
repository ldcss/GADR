# 2. Default service key for Dynamo DB sessions

Date: 2019-02-28

## Status

Accepted

## Context

Encryption keys for frontend user sessions are provided in environment variables and cycled during every release. 

This has resulted in one incident of losing syncronisation, causing errors for users when services scale up and then scale down.

## Decision

We will use a AWS owned Customer Master Key for the Sessions Dynamo DB tables to encrypt session tokens, and not push encryption keys into containers.

Table names                                       |
--------------------------------------------------|
refunds-sessions-front-<opg_stackname>            |
refunds-sessions-caseworker-front-<opg_stackname> |

## Consequences

Using a AWS owned CMK, as opposed to a AWS managed CMK, means there will be no KMS level audit trail for DynamoDB encryption within CloudTrail.

Release processes will be simpler and less prone to config drift.

Config management by Salt is reduced.

Application code will be updated to use the Default Service Key, and not the keys provided by config management.

## People

Involved: Matt Machell, Andrew Pearce, Richard McHale and Neil Smith

Signed off by Matt Machell

Joel Samuel (MoJ) was consulted.
