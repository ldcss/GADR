# 7. Only manage certain netfilter chains in kubernetes machines

Date: 2019-07-25

Status
------

Accepted

Context
-------

When using the puppetlabs firewall module, one of the recommended
settings is to purge all rules not managed by puppet:

```puppet
resources { 'firewall':
  purge => true,
}
```

Since kubernetes and calico perform networking and load balancing at the
kernel level, this means puppet finds itself with hundreds of rules to
purge every 30 minutes.

The firewall module also has an undocumented feature that lets you
manage individual netfilter chains:

```puppet
# This will remove all `-A INPUT` rules unless they're either (a)
# managed by puppet or (b) contain `--comment "you can trust me ;)"`.
firewallchain { 'INPUT:filter:IPv4':
  ensure => 'present',
  purge  => true,
  ignore => [
    '--comment "you can trust me ;)"',
  ],
}
```

This doesn't work in conjunction with `purge => true` for all firewall
resources. If we use `firewallchain` resources instead, then any chains
we don't explicitly define will be ignored by puppet. So, for example,
if we define only `INPUT:filter:IPv4`, then any existing `OUTPUT` rules
will be ignored rather than purged by puppet.

Decision
--------

We will only manage INPUT, OUTPUT, and FORWARD chains on kubernetes
machines. We will specifically whitelist particular lines known to be
used in those chains by kubernetes and calico.

Consequences
------------

As of writing this, it means we now have two firewall profiles
(`networking::firewall` and `kubernetes::firewall`), and they share most
of their code. We should probably split that `purge => true` line out of
the central firewall profile and come up with a single structure that
works more broadly.

Additionally, docker itself performs its own networking, so we'll want
to do something like this for the `docker` profile, but with different
exceptions in the chains we manage.

Security consequences: unknown.
