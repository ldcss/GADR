# 4. Roll our own kubernetes profiles

Date: 2019-07-25

Status
------

Accepted

Context
-------

Puppetlabs maintains [a kubernetes module][1] in the forge, and Rancher
maintains software for managing multiple clusters running anywhere.

The puppetlabs module claims to support Debian, but, in practice, it
appears to only support Ubuntu. We tried forking it and making changes
to get it working, but it was a rabbithole of error after error. Also,
their solution to managing SSL keys was to generate them locally and
store them all in hiera, which was cumbersome. They also didn't support
managing the CIDRs for the internal network.

Rancher seemed very nice at first, but it was unstable in practice.
Despite running a highly available set of control nodes, bringing one
down did in fact break the cluster. Also, if /var/lib/docker filled up
on any machine, the only solution was to destroy and recreate the entire
cluster.

My assessment of the puppetlabs module is that it tries to do too much
on its own. My assessment of rancher is that it's not yet stable enough
to rely on.

[1]: https://forge.puppet.com/puppetlabs/kubernetes

Decision
--------

We will roll our own kubernetes profiles instead of relying on someone
else's solution.

Consequences
------------

While our profiles are sufficient for creating an environment where
kubernetes can flourish, bootstrapping must be done outside of puppet,
by hand. It's not ideal, but it also shouldn't come up very often.

We haven't yet tried upgrading docker or kubernetes on an existing
cluster, but it's easy to imagine that being tricky if we have to do it
by hand.

It's worth checking back on rancher in a year or so to see if they've
improved.
