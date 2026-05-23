# 2. Sprout Fails Before Receiving Request

Date: 2018-06-17

## Status

Accepted

## Context

A sprout node fails before receiving a request from the P-CSCF, and the request fails.

## Decision

P-CSCF retries to sprout2

## Consequences

If sprout2 gets no failure, it'll send request to Homestead, or P-CSCF retries.

## Flow Chart

![sprout-initial-request](http://www.projectclearwater.org/wp-content/uploads/2014/04/sprout-initial-request.png)