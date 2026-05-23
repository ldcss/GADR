# 5. using aws ec2 as platform

Date: 2020-05-24

## Status

Accepted

## Context

I'm having lots of issues trying to detect and inject the IP address of the
 container to the env var so the etcd cluster can get up.

I can start it in single node, but I have no progress with the clustering.

I'm running out of time...

To speed up deployments, I can create my own AMI images with
 all the needed packages, and launch them from the provisioning system, 
 Terraform.  Then, using a Configuration Management Tool like Puppet or
 Ansible I could finish the configuration to adapt to the environment.


## Decision

After failing trying to use AWS ECS to launch an etcd cluster, I have switched
 to use AMI's instead of Docker containers.

This way I have to do a lot of things, but I think it will be easier to see
 progress.

I'm going to build my own images using Packer.  I used veewee before, but
 Packer is not so different.

Another option could be to use a cloud-init and a APT repository, but I have
 not enough time to make everything it can need.

I need to use Terraform to create the infrastructure and provision network,
 security groups, and load balancers.

Also, this way I can provision the rest of the instances I want, like Prometheus
 and Taurus (for benchmarking).

To manage configuration, I'm going to use Ansible.  More about this later.

## Consequences

Lot of time has been ruined trying to make the etcd cluster work in docker.  I 
 need to work faster and that means lots of typos and I don't want, but some
 bests practices would be affected.
