# 10. Use nginx for simple HTTPS proxies

Date: 2020-01-27

Status
------

Accepted

Context
-------

We currently use Apache on all our web hosts. While writing a profile
for forwarding HTTPS to a local HTTP port, I found that the puppet
Apache module didn't provide a simple approach to this. I would have had
to use `mod_proxy` and then add custom fragments.

On the other hand, if I went with nginx instead of Apache, such a proxy
could be configured with a single line:

    proxy => "http://localhost:${port}",

This carries with it a cost however. If we use nginx in this one case,
then we can no longer claim to use a single web server, as we'll be
using Apache on some servers and nginx on others.

Decision
--------

We will use nginx for simple cases where all we need is to forward to a
local port.

Consequences
------------

Forwarding https traffic to a local port is very easy. We now use both
nginx and Apache.
