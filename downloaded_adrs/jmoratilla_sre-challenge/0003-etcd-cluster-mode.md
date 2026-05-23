# 3. etcd cluster mode

Date: 2020-05-21

## Status

Draft

## Context

Etcd has three ways to setup a cluster:

- Statically: setting all the IP's and listeners of the cluster members from
 command line
- Dynamically: using an external etcd cluster (https://discovery.etcd.io/new?size=X)
- Dynamically: using a DNS SRV record.

I have tested two first options, and found that the main problem is that the
 cluster member is identified by its name AND it's peer URL, not only its name.
  That's make my job very difficult as I cannot just open a 0.0.0.0/0 listener
  for listening and peering with other members.  It has to use always its IP.

I need to find a way to identify each etcd cluster member with the IP address
 for peering.
 
## Decision

There is an option: setting a network in docker / aws vpc and force the IP
 address used for that container / instance.


 

## Consequences

It would work, but I cannot envision now what other issues it could produce in
 a future escenario.  I don't like the idea, but I haven't found anything
 better just now.

