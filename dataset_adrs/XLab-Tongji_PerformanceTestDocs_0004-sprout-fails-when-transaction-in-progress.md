# 4. Sprout Fails When Transaction In Progress

Date: 2018-06-17

## Status

Accepted

## Context

A sprout node fails while a transaction is in progress, the transaction fails.

## Decision

Either the UE will retry automatically or it will display an error to the user, who should retry. Transaction fail can't be routed to sprout2 (As from that point on the P-CSCF will not retry the transaction).

## Consequences

UE/user retries, or transaction fails

## Flow Chart

![sprout-pending-transaction](http://www.projectclearwater.org/wp-content/uploads/2014/02/sprout-pending-transaction.png)