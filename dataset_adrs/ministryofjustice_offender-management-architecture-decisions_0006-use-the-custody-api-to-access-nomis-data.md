# 6. Use the Custody API to access NOMIS data

Date: 2018-10-19

## Status

Accepted

Amended by [16. Use the Elite2 API to access NOMIS data](0016-use-elite2-api.md)

## Context

Our main source of data on prisoners and prison staff which we need for
allocations is NOMIS.

There are now four APIs into NOMIS providing general data access, with varying
approaches to presenting the data and authentication. We do not want to add to
this duplication.

The APIs which have been developed more recently are more under the control of
HMPPS than the earlier ones (which were developed by a supplier). That gives us
more flexibility around how we work with them and makes it possible to get
changes into production more quickly. Using one of the newer APIs should mean
that we are less blocked by delays around API changes than we have been on our
work on Visit someone in prison.

It has been agreed by the HMPPS technical community that we would like to move
all clients to use the Custody API in preference to the other APIs over time.
Although that work has not yet been prioritised, using the Custody API for new
applications will reduce the work needed in future to align our API usage.

The Custody API has been designed to give a more direct view of the data in
NOMIS than the previous APIs have been - earlier approaches have favoured
implementing specific endpoints to meet the needs of service teams rather than
giving a more comprehensive view of all the data.

## Decision

We will use the Custody API to access the NOMIS data we need.

We will work with the team in Sheffield on development of the Custody API to
add support for accessing the data we need.

## Consequences

We will be aligned with the agreed approach to APIs in HMPPS.

We will reduce dependencies between teams by taking on much of the API
development work ourselves, which should help us move faster after an initial
learning period.

We will need to dedicate some time to learn more about Java development and how
to use the patterns already established in the Custody API. This will include
several days of pairing with people from Sheffield.

We will need ongoing support from the team in Sheffield to review pull requests
and deploy API changes for us.

We will reduce the pressure on the API developers in Sheffield over time by
taking on much of the work ourselves.

We will be able to use system-to-system authentication rather than having to
authenticate API requests as the logged-in user (as some of the earlier APIs
do). The latter approach is not possible to follow consistently when we need to
request data from several systems, as we know we need to.

We may find that it is much more efficient to request exactly the data we need
from the Custody API, rather than making a large number of requests and then
constructing the data structures ourselves, or requesting a large volume of
data and then filtering most of it out ourselves. Relational databases are
well-suited to doing this work. That may mean that we need to consider whether
to expand the scope of the Custody API to support filtering of lists, or
requesting specific fields. We will discuss these needs with the team in
Sheffield if they arise.
