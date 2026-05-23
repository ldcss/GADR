# 8. Dedicate separate HAProxy machines for load-balancing kubernetes

Date: 2019-07-25

Status
------

Accepted

Context
-------

With three controller nodes all listening on 6443, they need a single IP
address they can use to represent "the kubernetes master." Additionally,
each worker node listens on 30000-32767 in order to expose NodePort
services to the outside world. Rather than choose a particular worker
node to talk to, it makes sense to load-balance these requests as well
to whichever worker nodes are currently online.

What's written above is straightforward enough to add to our current
HAProxy config.

However, kubernetes doesn't provide any support for claiming IP
addresses outside its internal network. Rather, kubernetes merely
indicates that it wants an IP address for a service.

For example, let's say we have a web service that is listening on ports
80 and 443. If we set its exposure to LoadBalancer, then kubernetes will
indicate that and set some NodePort mappings. So, for example, it might
map 80:32689 and 443:31268.

It's then our job to do the following, outside kubernetes:

1.  Notice a new service requesting to be type LoadBalancer.
2.  Choose an IP address that isn't already in use.
3.  Configure our load balancers to claim that floating IP address.
4.  Configure our load balancers to round robin 80 and 443 requests for
    that IP address to the kubernetes worker nodes over 32689 and 31268,
    respectively.

It would be good if we didn't have to do that by hand. If we do automate
it, that means our HAProxy config could be changing routinely, which
could have an affect on other production services.

Decision
--------

Kubernetes gets its own HAProxy servers, separate from the ones
currently configured by puppet. For the time being, puppet will
configure them, but it also provides a simple list of peer IP addresses
so that they will one day be capable of configuring themselves.

Consequences
------------

We can make changes to the load balancers for kubernetes without
worrying about breaking access to our first-class services already in
production. Even though the details of these servers are very similar,
this separation lets us view these HAProxy machines not as load
balancers but rather as highly available gateways to kubernetes.
