# 5. Homestead/Dime Fails

Date: 2018-06-17

## Status

Accepted

## Context

Homestead instance fails before receiving request from sprout. 

## Decision

Homestead’s HTTP interface is simple. If one homestead instance does not respond to sprout, sprout tries a different one

## Consequences

Request fails or succeeds

## Flow Chart

![homestead_fail](http://www.projectclearwater.org/wp-content/uploads/2013/10/homestead_fail.png)