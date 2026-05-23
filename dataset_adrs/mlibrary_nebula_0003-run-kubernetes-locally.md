# 3. Run kubernetes locally

Date: 2019-07-25

Status
------

Accepted

Context
-------

There are many cloud kubernetes offerings (Amazon, Microsoft, and Google
all offer it), and part of the appeal in general is to not have to think
about where the servers are and what kind of maintenance they need.

However, we already operate servers in three datacenters, and we fully
manage one of those. We may prefer this not to be the case, but as of
writing this, we deal with bare-metal servers regardless of what we'd
prefer. Adding ec2 instances costs extra money, where running additional
software on servers (with an electric bill we're already paying) costs
the labor of setting it up.

The attitude of the field so far appears to be "definitely just run it
in AKS," but the field is largely made up of people whose primary
interests are reliability and profits. As a digital academic library, we
also have those interests, but we have an additional responsibility to
always have our own copy of everything.

Decision
--------

We will provide kubernetes clusters at our datacenters with the
possibility of expanding outward into cloud providers as needed.

Consequences
------------

By providing a service that mirrors a cloud service, we can use the same
code and configuration to deploy locally and remotely. We'll need to
figure out how we want to manage applications and how we'll want them to
scale depending on where they live. Since developers will essentially be
deploying to three different clusters, we'll need to decide how they
should do that.
