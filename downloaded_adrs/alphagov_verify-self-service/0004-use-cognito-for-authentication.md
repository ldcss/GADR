# 4. Use Cognito for authentication (via APIs)

Date: 2019-08-12

## Status

Accepted

## Context

Given our application allows making changes to the federation configuration,
it is neccessary to secure the service appropriately. The same instance
will be accessed by different users with varying level of permissions.
Therefore we need to have a strong authentication and user management in place.
Our key authentication requirements are:
- Secure
- Flexible and extendable
- Cost effective
- Multi-factor authentication (MFA) support
- GDPR compliant

## Decision

Based on our requirements, we decided to use Amazon Cognito - a service provided by AWS.
Amazon Cognito satisfies all the requirements and offers an easy way to implement 
authentication in our application.

Initially we integrated with Cognito using OAuth. However, we soon realized the
customisation options are very limited. In the interest of more flexibility and
a more consistent user journey we have decided to integrate with Cognito using AWS SDK and APIs.

In terms of cost, Cognito is free under 50,000 monthly active user. We never envision hitting the threshold.

Furthermore, to ease our implementation using the SDK we have imported Devise to provide
the app with an authentication framework.


## Consequences

* We do not store any passwords or personal details. All the data is in Cognito.
* For audit purposes, in the logs we only store the unique ID of the user.
* Given Cognito is an AWS service, there's no need to manage secrets as we can use IAM roles.
* It creates a dependency on an AWS service.
* We can use Terraform to configure and deploy Cognito with the rest of our infrastructure.
* Limited supported within GDS as no other teams are using it.


