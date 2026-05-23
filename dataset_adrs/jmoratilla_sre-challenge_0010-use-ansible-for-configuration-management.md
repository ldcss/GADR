# 10. use ansible for configuration management

Date: 2020-05-26

## Status

Accepted

## Context

When I decided to use AMI's instead of docker containers, I knew I had to 
 use some tool for configuration management.  

This tool would help me to execute configuration tasks.  But as my intention
 is to create an inmutable system, I don't want to manage changes, just set
 the resources.

For doing this I could implement Puppet, Chef, or Ansible.  I have experience
 with all of them, but recently I have been working more with Ansible.  And for
 a challenge like this, I prefer something modern, without servers.

## Decision

I have used Ansible to configure all the services for the three kind of nodes
 in the challenge: etcd, monitor, and benchmark.

## Consequences

Ansible is simple to do quick work, and now that's my goal now.  For future
 revisions, I would think more about what configuration management system would
 be better for me.

