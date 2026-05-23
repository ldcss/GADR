# 2. Use Debian as a host OS

Date: 2020-06-07

## Status

Accepted

## Context

I used the following points to make my decision:

- Ubuntu 20.04 uses a unique auto-installation method, which is generally nice, but completely non-transferable
- `snapd` remains controversial, but using Ubuntu systems forces that path more nowadays
- Debian should be relatively "install and forget"
- Centos is more opinionated about some things like how network configuration is done
- Centos doesn't do automatic security upgrades, at least not in the same way RHEL advertises
- I've successfully used Debian before for this role, before trying out Ubuntu again
- Remastering a Debian iso with the preseed configuration can result in a one-button install process

## Decision

Use Debian buster as the hypervisor OS, with an automated installation via Debian preseeding.
