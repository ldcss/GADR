# 2. Manage user permissions in Fusion Auth

Date: 2020-09-14

## Status

Accepted

## Context
In Armadillo:

* A cohort is an OpenID application
* The researcher needs a `ROLE_<STUDY>_RESEARCHER` on the application to read data
in shared folder `<study>`

Requirements on who manages what:

* User and permission management is done by representatives of the consortium and cohort
* The identity of the user is federated to their local institution
* Representatives of the cohort administer the study researchers’ admission to their cohort
* Representatives of the consortium can see which users have which roles on which cohort

## Decision

Implement this in Fusion Auth, plus a (modest) administration UI.

* The users register themselves.
* A cohort representative explicitly creates a registration for the researcher in the application,
with one or more roles.

### Administration

Application-specific permissions are not available in Fusion Auth.
In other products they tend to be rather complicated to configure.

Create an edge service that enforces the permissions and uses
an api key to administer them through the Fusion Auth API.

## Consequences

* Need to build the service and a UI
* Clear specific UIs for the cohort manager and consortium manager
* The cohort manager UI is deployed within the armadillo-cohort deployment
* The consortium manager UI is deployed together with the Fusion-auth deployment
* Only need only 1 Fusion-auth server for a consortium

## Alternative: study groups

* Consortium representative puts user in study group
* Cohort representative creates user registration for cohort (or enables auto registration)
* Cohort representative gives study group roles on application

This is more coarse-grained, leaves more power with the consortium, less administration for the cohort.

We decided *against* this because the following flow should *not* be possible:

If a cohort registers a user who is in one study group and then later
the consortium adds the user to another study group, the user can perform analyses
on that second study group's exports without the cohort's explicit permission.
