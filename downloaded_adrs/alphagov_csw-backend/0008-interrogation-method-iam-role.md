# 8. Interrogation method - IAM role

Date: 2017-11-22

## Status

Accepted

## Context

Within GDS product teams operate autonomously and tech-ops 
is relatively new. There is no central administration of 
AWS. There is a shared authentication model but it is not 
used everywhere. 

Teams are busy with their own mission work and don't have 
time allocated to standardisation or security work. 

To get things built in a client AWS account we need to: 
* negotiate time from the product team 
* provide them with the code to build the resources
* code review with them to reassure them that it's OK to 
run our code in their environments 
* repeat for each team we engage

We want to make it easy and low-risk for a team to engage 
with us. 

If there were centralised management of all accounts, the 
sensible way to do this would be by configuration the 
config service with a set of config rules administered 
and maintained centrally by Cyber Security. 

These rules would be largely triggered by CloudTrail 
events notifying us of compliance as soon as resouces were
created or changed. 

However this approach would involve quite a large number 
of resources deployed into each client AWS account which 
means a longer and costlier engagement process. 

The simplest way to do this is by provisioning an IAM role 
and associated policy. That way we can work from the 
principle of least privilege, granting us only the access 
we need to run our audit making it low risk. 

By providing the role and policy definition in a Terraform
module we can also ensure that it requires little work by 
client account holders. 

The advantage of the IAM mechanism is that since we're 
querying the configuration of the user account directly 
via the API it is very easy to tell whether our service 
has been tampered with - the only thing that can change 
is the definition of our policy which we can check. 

In the config service model there are more moving parts 
within the client account which could be switched off,
altered or intercepted. 

## Decision

Create a terraform module which creates an IAM role and 
associated policy granting primarily read-only access 
(Get, List, Describe API calls) working from the 
principle of least privilege. 

## Consequences

This is a short-term solution. The longer-term vision is 
to implement using the config service if we can obtain 
centralised access to deploy the changes across all 
accounts. 

Our model is pull instead of push. We would prefer a push
model with client accounts notifying us directly of 
changes - hence the longer-term vision for the config 
service. 

We operate on a schedule or on demand rather than triggered 
by change events. 

We should code in such a way as to enable us to re-use the
code in the config service in future. 
