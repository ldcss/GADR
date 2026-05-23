# 2. use load balancer

Date: 2018-11-21

## Status

Accepted

## Context

The ability to update/upgrade our servers for security or testing purposes is
key. We will have at least two virtual machines sharing a mounted directory on
each that will contain files that all servers can view. The biggest benefit will
be the Web Application Firewall that will be applied to all traffic that is
targeted to the `library.princeton.edu`. Using deep packet inspection malicious
patterns will be diverted away.

## Decision

We will create

* a smb/cifs and/or nfs mount that will be present on all nodes behind the
  loadbalancer
* we will create a service (Kemp terminology) called `library.princeton.edu`
* we will create nodes that will mount the aforementioned drives
* we will implement SolrCloud on a remote endpoint that all nodes can read and
  write to
* we will implement remote database (mariadb) that all nodes can read/write to

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.

* It will be trickier to launch and test the website locally using Vagrant
* We will need to have a clearly defined deployment strategy
* The service will be more robust and allow upgrades without disruption
