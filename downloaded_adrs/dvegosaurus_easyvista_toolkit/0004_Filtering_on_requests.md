# Filtering on requests
date : 2019/10/03

## Status
proposed

## Context
We'd like to be able to pull requests by recipient and/or requester but the */requests* endpoint does not return those values straigh away. Instead they are embedded in JSON format within the fields *REQUESTOR* and *RECIPIENT*.

This means that we can't use */search=recipient~"recipientname"* to get the requests linked to a particular user.

## Decision
We will use the *where-object* from powershell to filter on requestor and/or recipient. This will be implemented like so :
- Using a *maxrows* parameter to force easyvista to return more than the default 100 results when requesting */requests*
- Using a powershell scritpblock built in the relevants cmdlets to filter the result by requestor and/or recipient.

## Consequences
### Pros
- none
### Cons
- Requesting for requests will be slower
- Requesting for requests will be less reliable when filtering on requestor and/or recipient:
    - The maxrows parameter will determine the set of data on which the filtering will take place 

*__note__: we might wan't to implement a ways to sort result from queries to /requests by date either by default or using cmdlets's parameters*
