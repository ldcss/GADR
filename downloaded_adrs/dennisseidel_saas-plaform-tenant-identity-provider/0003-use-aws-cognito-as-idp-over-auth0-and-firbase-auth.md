# 3. Use AWS Cognito as IDP over Auth0 and Firebase Auth

Date: 2019-02-05

## Status

Accepted

## Context

We need to decide for a hosted identity provider. An the different option are AWS Cogntio, Auth0 and Firebase Auth.

## Decision

We select AWS Cogntio as the hosted IDP.

## Consequences

Because it offers the interfaces of the standard OpenIDConnect Providers as well as a SSO offering and a hosted login/signup page while having a sufficient free tier and being cheaper at scale than Auth0. Firebase Auth was to limited to it's own libraries and focuses on mobile even though it is fully free. Further Cognito is GDPR and HIPPA compliant: 
* https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html
* https://www.aptible.com/hipaa/what-is-a-baa/#what-is-a-baa
* https://aws.amazon.com/de/compliance/gdpr-center/service-capabilities/