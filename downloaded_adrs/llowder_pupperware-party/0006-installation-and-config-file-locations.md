# 6. Installation and Config File Locations

Date: 2019-03-12

## Status

Accepted

## Context

Software needs to be installed in order to be useful, and also normally needs config files. Where to put these and where to install to can have an impact on user experience.

## Decision

We will follow the example set by Puppet, since this software is part of that ecosystem

## Consequences

The location of an installation and config files can have a significant impact on overall user experience. If you put things in common places, it will be easier for the user to know where to look and what to expect. Putting things in weird places will lead to frustration of the user.
In our case, the two main choices are to follow the Linux Filesystem Hierarchy (LFH) recommendations and install to /opt/pupperware-party and place global config files in /etc/opt/pupperware-party/ or to follow the conventions of Puppet's All in One packaging, and install to /opt/pupperware-party and place global config files into /etc/pupperware-party/.
While following the LFH may be more pedantically correct, I beleive it will be less confusing to puppet users to follow the conventions that Puppet uses.
