# 2. Ansible: do not use local connections

Date: 2020-05-02

## Status

Accepted

## Context

Since this project targets a local workstation and is aimed to be run by the same
exact localhost, should we use ansible's connection local for ansible.cfg and localhost
as a host in all the playbooks?

## Decision

We will model the ansible playbook hosts as separate groups and form a full inventory
of them. The inventory will be assigned to localhost or 127.0.0.1 ip.

The logical explanation of this is having a set of playbooks that can be run from everywhere
for two reasons
* learn and expirement with the main ansible goal, i.e. setup remote hosts
* re-use this project in the future for more than our workstation

## Consequences

Implementing this decision will complicate the ansible playbooks more.
