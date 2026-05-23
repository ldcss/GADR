# 5. Stack kubernetes controllers with etcd

Date: 2019-07-25

Status
------

Accepted

Context
-------

There are three basic ways to lay out controller nodes in a kubernetes
cluster:

1.  A single master is the easiest way to do it, but if that node is
    ever unavailable, then the entire cluster is unavailable.

2.  A highly-available group of at least three controller nodes that
    also run etcd.

3.  Two highly-available groups: one of at least three controller nodes,
    and the other of at least three etcd nodes.

The kubernetes website has [a detailed rundown][1], but it boils down to
this: high availability complicates the set-up significantly, and
separating etcd from the control plane complicates it yet more.

However, if we want to allocate a lot of resources to high availability
in our kubernetes clusters, then etcd is a nice seam to further divide
responsibility as we scale up the count of control nodes.

[1]: https://kubernetes.io/docs/setup/independent/ha-topology/

Decision
--------

We will start with the middle path of minimal (but extant) high
availability. Low availability would fail to grant us a lot of what
makes kubernetes worthwhile, but we're just not in a place where we're
ready to commit the extra resources to get the highest availability
possible.

Consequences
------------

If we start growing our pool of stacked controller nodes beyond 5, then
we should consider revisiting this decision.
