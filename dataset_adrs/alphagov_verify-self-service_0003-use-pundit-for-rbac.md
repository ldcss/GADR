# 3. Use Pundit for RBAC, Store Roles in Cognito and use Cognito Group for teams

Date: 2019-07-30

## Status

Accepted

## Context

As with any modern web system there is a need to secure the application with
strong authentication and Role Based Access Control (RBAC). RBAC allows us to
create permissions, apply them to roles and associates roles with users. From
this we can restrict what users can do and see within the application based on
their role. In addition to this we also had to investigate where to store role
information and define teams to support our use of RBAC.

## Decision

After some investigation and discussion into various ways of implementing RBAC
within Ruby we have decided to implement the Pundit Ruby gem within the Verify
Self Service application. This gem provides us with a way of creating policies
which apply to the app as a whole and to individual classes within the
application.

We have chosen pundit for a number of reasons. The first is that it seems
relatively easy to implement within our application. A proof of concept was
created in a few hours which restricted creating new components within the
application to those who hold the `gds` or `dev` roles. Policies and permissions
are defined in code as plain Ruby objects which are easy to understand and
simple to implement. This ease of implementation and an appearance of providing
the fuctionality we are seeking we believe makes pundit a good candidate for
implementing RBAC within our application.

In addition to this we are aware of prior-art use within GDS on the GOV.UK
project. Finally we have found a lot of documentation and articles about how to
implement and use pundit.

Role information we have decided to store in a custom field within our cognito
instance. This will take the form of a comma seperated list which will be split
into an array of roles for use within the application. This method allows us to
keep all use information together within AWS Cognito and means that the only way
role information can be changed is via SDK calls to AWS Cognito.

Finally we understand there is a need to define teams within our application. We
have decided that a team is analogous to an AWS Cognito group. This allows a
user to be part of one more groups and for a group to hold one or more users. We
can easily query group membership using the AWS Cognito SDK and check for a
users membership to a specific group.

## Consequences

* By using Pundit we will tie ourselves to a specific way of doing RBAC.
* AWS Cognito groups don't have unique identifiers other than name which means
  all team names must be unique
* Roles aren't specifically defined within the model of the application
* We don't need to store user roles or mappings within our application but it's 
managed in a single place (Cognito)

