# 1. PoS decisions

Date: 2019-11-12

## Status

Accepted

## Context

For the Proof of Skill assignment several auxillary technology have been used on top of the required terraform. As terraform
as a infrastructure as source is a given in the assignment, others will be explained here. 
## Decision

### Repeatable project creation
The use of ansible as a project templater. Ansible is selected to have a reentry method to create projects from a template. In this case this is more used for documentation than template but it is used
to illustrate its use. The author is aware that ask nicely is using Puppet, but the author is more familliar with ansible and as this is an anxillary 
tool this one is selected over puppet. 
 


## Consequences

Extra tooling adds complexity to the project. It is believed by the author that is offset by the ease of reuse and inherent documentation of the project. 
