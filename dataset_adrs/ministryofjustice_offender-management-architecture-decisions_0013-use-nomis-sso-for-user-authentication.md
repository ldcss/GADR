# 13. Use NOMIS SSO for user authentication

Date: 2018-11-22

## Status

Accepted

## Context

### Users

We need to authenticate users in order for them to access the service. We will
have users from prisons and probation services, both public and private in both
cases.

We expect our earliest users to be prison-based Senior Probation Officers and
Offender Management Unit administrative staff, followed by Prison Offender
Managers and community-based Senior Probation Officers. It's possible that we
will also need to enable Community Offender Managers to log in in future, but
we don't yet know what we might build for them so that's not certain.

### Existing options

We do not want to build user authentication from scratch ourselves. There are
two shared approaches for authenticating users which are currently in use with
HMPPS digital services, both of which are based on OAuth2 and support
role-based access control:

- MOJ Signon
- NOMIS OAuth server, including new SSO functionality

Both of these originally emerged from the needs around one or two services, and
were subsequently adopted by a few other services. A discovery aiming to
develop a clearer strategic direction in this space has recently concluded, and
found that neither of the two existing approaches meet the needs of users and
teams well across the range of HMPPS services and their user groups. For now,
though, these are the two available options to consider.

If we use MOJ Signon, we would use the authorization code grant type. The team
are familiar with MOJ Signon from their work on Visit someone in prison.

If we use NOMIS Auth, we would need to decide whether to use the new SSO
functionality with the authorization code grant type (which has been developed
recently and is not yet available in production) from the beginning, or whether
to have our own login page and use the password grant type initially, only
switching over to use the SSO approach when it's available in production.

The SSO approach means that we would have less to build ourselves, and wouldn't
need to handle users' passwords, and those advantages mean more generally that
it's intended to replace existing use of the password grant type by other
services.

### Service

The services we're working on for Manage Offenders in Custody are seen as being
fairly closely related to a group of services which already use NOMIS Auth.

The users of our service who are working in prisons will need to have NOMIS
accounts anyway. Probation staff have so far not had NOMIS accounts, but
another service team (Home Detention Curfew) is using NOMIS Auth and intending
to create accounts for probation users for that service. The new web-based
services being built around NOMIS mean that users won't have to be on the
Quantum network to access the services, and in future it will be possible to
manage a NOMIS account without access to that network as well (for password
resets, updating profile info, managing roles etc).

Some of our users (OMU admins in some prisons) will already have MOJ Signon
accounts in order to use Visit someone in prison, but many won't be doing that
already (and they would all have NOMIS accounts anyway).

### Route to production

We expect that matching up data between NOMIS and Delius will be the main
challenge for us, and that we'll only be able to see how well that works in
production because there aren't any pre-production environments with related
data across the two systems. We're keen to get into production as soon as we
can for that reason.

However we don't currently expect to have any way of getting access to the
Delius API for some months, which reduces the urgency of this consideration.
Our priority now is to make decisions which enable us to make progress with
development.

The NOMIS Auth team expect the new SSO to be in production within the next
couple of months, which is very likely to be before we get Delius API access.

## Decision

We will use NOMIS accounts for authenticating users of the allocation manager.

We will use NOMIS SSO from the start, rather than building our own login page.

## Consequences

All our users will need NOMIS accounts. This will probably include some users
who are not prison-based in future.

We need the newer NOMIS SSO functionality to be deployed to production before
we can get our applications working in production. If this is unexpectedly
delayed past the point when we need it, we will need to consider implementing
the password grant type to use temporarily.
