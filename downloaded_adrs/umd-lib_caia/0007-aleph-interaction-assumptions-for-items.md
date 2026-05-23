# 0006 - Aleph Interaction Assumptions for "items"

Date: June 24, 2020

## Context

For "items", it is assumed that Aleph always provides a list of new/updated
items that occurred within the date range provided.

## Consequences

The application does only minimal processing on the list of new and updated
items returned by Aleph.

There are two requests made to CaiaSoft, one for the "new" items, and one
for the "updated" items. The "last_success" file (used to determine the
start time for the next request) will always be updated, unless CaiaSoft
cannot be contacted (on either request), or CaiaSoft indicates that the
request failed (returned a "success" flag on "N").

There is currently no provision for resubmitting items that were rejected
or had errors, as they are currently expected to be handled manually. 
