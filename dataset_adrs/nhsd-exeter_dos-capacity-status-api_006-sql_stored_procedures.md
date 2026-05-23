# 006 - SQL Stored Procedures

- Date: 2020/02/24
- Status: Proposed
- Deciders: Daniel Stefaniuk, Jonathan Pearce, Matthew Begley

## Context

In order to protect DoS services from having capacity status information updated by users of the Capacity Status API that do not have the required permissions to do so. Core DoS maintains user services permissions, therefore the API requires an interface to Core DoS to be able to validate that an API user is able to update capacity status information of the requested service.

## Decision

In a previous ADR it was decided that the API itself would not hold or maintain user services permissions (please refer to ADR-004), and so the API will require a route (or interface) to Core DoS where user services permissions are stored and maintained. The following options were considered:

- Use of current Core DoS APIs
- Creation of an SQL stored procedure, which is lodged in the Core DoS database
- Creation of a query in the 'DoS' module of the Capacity Status API

Investigation was performed into the existing Core DoS APIs and it was found that although it was possible to combine a couple of the APIs together in order to get to the desired result, the complexity and processing (wasted) to do so simply was not viable. The existing APIs offered no direct route to the information the Capacity Status API required.

A simple query, therefore, (starting from the target service, and propagating up through any parents) will be created to determine whether the API user has permissions to update either the target service OR a parent of the target service. It is envisaged that this query will run on the Core Database and will yield a result in a far more efficient and much faster way than by the indirect route of the existing APIs.

So as not to impact on Core DoS timescales, and so we (the developers of the Capacity Status API) could alter the logic of the query and to fine tune it, the decision was to implement the query as part of the Capacity Status API for private Beta. This then has no affect on Core Dos, and means that we have no dependency with the Core DoS team. In addition, it was considered that Core DoS changes in this area are unlikely. Furthermore, it has already been decided that the API will contain a separate 'DoS' module (refer to ADR-004). The query will reside in this module which the core API code will invoke, meaning only the 'DoS' module has a coupling with Core DoS, hence reducing unlikely (although potential) dependency issues should this area in Core DoS change.

## Consequences

- Using a direct query is by far faster and more efficient, reducing processing time and complexity.
- Lodging the query in a stored procedure in the Core DoS database may affect turn around or response time should we need to rapidly change the query while in private beta development stage. Having the query in the Capacity Status API code base enables us to be able to work, adjust, and fine tune it during the private Beta phase. Once we have assessed that the query is stable, we will revisit the decision to lodge the query in the Core DoS database.
- This introduces a coupling with the Core DoS user services permission data model, although this risk is countered by the fact that this area of Core DoS is unlikely to change, and any coupling with Core DoS will be implemented in a separate 'DoS' module within the API, thus reducing potential impact to a minimum.
