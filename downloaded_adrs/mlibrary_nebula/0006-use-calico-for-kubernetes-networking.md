# 6. Use calico for kubernetes networking

Date: 2019-07-25

Status
------

Accepted

Context
-------

Kubernetes requires an internal private network, just for its pods and
services (i.e. not for physical/virtual nodes). It has specific
expectations, but it doesn't actually provide networking itself. There
are a few options for internal networking: flannel, calico, canal, and
weave.

Of these, Flannel is the most popular. It's known for being easy to set
up and then never having problems ever. The network it creates is a
layer 3 IPv4 overlay network that spans across every node in the
cluster. Each node gets its own subnet for allocating internal IP
addresses for docker containers.

Project Calico is also popular, but is less simple and (allegedly) more
performant. The network it creates isn't an overlay but rather a layer 3
network using the BGP protocol to route packets between hosts.

Canal is a combination of flannel and calico. It's not a project anymore
because it collaborated itself out of existence by making pull requests
to flannel and calico until they worked well enough together that there
was nothing extra for canal to do. People still use the word "canal" to
refer to using a combination of flannel and calico.

Weave Net creates a mesh overlay network between each of the nodes in
the cluster. Each host becomes a router, and they're always exchanging
topology information with each other. One of weave's unique features is
that it can (with some network overhead) encrypt all routed traffic.

The rancher project wrote [a pretty informative comparison][1] if you're
interested in more details.

[1]: https://rancher.com/blog/2019/2019-03-21-comparing-kubernetes-cni-providers-flannel-calico-canal-and-weave/

Decision
--------

We will use calico because it's rancher's default. It's easy enough to
set up.

Consequences
------------

As of yet unknown.
