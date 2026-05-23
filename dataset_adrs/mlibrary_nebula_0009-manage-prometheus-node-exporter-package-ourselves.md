# 9. Manage Prometheus node exporter package ourselves

Date: 2019-08-21

Status
------

Accepted

Context
-------

The Prometheus model is that nodes, applications, and services expose
metrics, and a Prometheus server scrapes them every 10 seconds. It's up
to the Prometheus server to organize metrics, track them over time, and
store them long-term.

However, it's up to each node to decide exactly what metrics it exposes.
For example, the node exporter (which exports general system metrics)
has changed the names of its metrics as it's changed versions. It's in
the apt repos for Debian and Ubuntu, but with different versions for
different releases.

So if we stick with Debian/Ubuntu-maintained packages, we might end up
with jessie machines running v0.11.2, stretch running v0.13.1, buster
running v0.16.0, and bionic running v0.18.1. In this case, we'd be using
one aggregation server to scrape four different types of metrics all
baring the same name.

Not only would this be cumbersome to aggregate, but also if someone at
Debian or Ubuntu did upgrade the exporter in a repo, then all time
series for computers using that repo would essentially be reset.

Decision
--------

We will manage our own version of the Prometheus node exporter in our
apt repository. Rather than mimic the existing Debian package, it will
only install the binary. Puppet will manage the users, groups,
services, and files.

Consequences
------------

We won't be able to depend on `apt-get dist-upgrade` for fixing security
vulnerabilities if any are found in the node exporter. We'll need to
regenerate our debs with patched versions when they come out.
