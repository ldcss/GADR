# 2. Use cognito for private beta

Date: 2018-07-05

## Status

Accepted

## Abstract

Use Cognito for buyer authentication and authorisation for Private Beta. Reconsider the approach after that.

## Context

Buyer organisations are developing Sign-In services which we will use for user authentication and authorisation in the longer term, but we need something more quickly to enable a private beta rollout. 

We need to provide restricted access to a small number of users during private beta, to support continued testing and iteration of the supply teacher framework service. We also expect to need a mechanism for user authentication and authorisation for the other frameworks. 

CCS may deliver a common buyer identity provider in the future. Using a single authentication service will reduce administration overheads because we won't have to manage a JML (Joiners Movers Leavers) process. For users it will also mean they don't have to remember yet another username and password combination.

However, we want to get moving quickly, and integration with DfE Sign-In and identifying an identity solution for the other frameworks will take time. For now, we want a simple sign-in service that we can integrate with quickly, to enable us to test and iterate the application.

Auth0 is already in use by another CCS digital service, Report Management Information, as recorded [in their decision records](https://github.com/Crown-Commercial-Service/ReportMI-ADRs/blob/master/doc/adr/0011-use-auth0-for-temporary-user-authentication.md). 

AWS Cognito is part of the AWS infrastructure and can be deployed using Terraform scripts according to [CCS #11. Use the same cloud architecture](https://github.com/Crown-Commercial-Service/CCS-Architecture-Decision-Records/blob/master/doc/adr/0011-use-the-same-cloud-architecture.md)

We may have many thousands of users and either solution needs to be paid for. Since we cannot predict when other identity providers come online.

Costs 

|users|cognito|auth0|
|------|------|-----|
|up to 7000| | £0| £0|
|9000| £0| $1350/month|
|50k|£0| unknown|
|additional|$0.00550 per user per month|unknown|

## Decision

We will use AWS Cognito for authentication on a temporary basis.

Cognito is tied in with our existing infrastructure approach and easy to integrate.

We acknowledge that we are incurring technical debt by not integrating immediately with DfE Sign-In, however we believe that this will let us move more quickly during development.

This decision will also allow us to gain a better understanding of the user needs around authentication before a decision around the final authentication solution for the other frameworks is made.

We will integrate with Cognito, configuring via our Terraform scripts, but will need to replace this later.

We will replace Cognito with the buyer authentication services from each buyer community, such as DfE, when they are available.

We will replace CMp Cognito service later in the development process when a common CCS buyer identity service is available.

## Consequences

We will integrate with Cognito, configuring via our Terraform scripts, but will need to replace this later.

We will need to add DfE identity provider integration when it is available.

We will work with other projects within CCS to establish the user needs around authentication, and feed into the decision around the strategic solution.

