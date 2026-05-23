# 0009 - Aleph "items" Endpoint Behavior

Date: June 30, 2020

## Context

The Aleph endpoint used by the "items" command to query for new or updated
accession items has the following behavior:

1) When querying the endpoint for the first time, a "starttime" parameter that
   is the "endtime" result from the last successful source response is provided.
   In this context, "last successful" means that the new and updated entries
   in the source response were successfully uploaded to CaiaSoft.
   The "endtime" parameter must _not_ be provided on the first request.

2) Every source response will include an "endtime" result that denotes the
   end time of the query.
     
3) If there are a large number of results, Aleph may return a non-empty
   "nextitem" entry in the response. This indicates that there are more entries
   to retrieve, and additional source requests should be made. When making
   requests for these additional entries:
   
   * The "starttime" parameter should be the same as the initial request
   * The "endtime" parameter should be the same as the "endtime" entry in
     the previous source response
   * The "nextitem" entry from the previous source response should be provided.

On the very first run of the "items" functionality, there is no previous
source response to derive the "starttime" from. This is handled by providing
a "default" source response. In the "default" source response, the "starttime"
should be a simple datestamp (i.e., a date without a time), in order to avoid
any timezone issues.
 
Note that other than the first run, all the timestamps used for the "starttime"
and "endtime" parameters are provided by Aleph. This avoids any issues regarding
out-of-sync clocks between the servers and timezone issues, because only Aleph
is providing the timestamps used for these parameters.

## Consequences

To support the "nextitem" continuation, the "items" steps run in multiple
iterations, where the result from the last iteration is used as the input to
the next iteration.

Each iteration consists of:

* Querying Aleph for the new/updated items
* Sending new items to the CaiaSoft endpoint
* Sending updated items to the CaiaSoft endpoint
* Storing the "last successful" result to use in the next iteration/job

The iterations operate within the context of a single job, and continue as long
as the Aleph response contains a non-empty "nextitem" entry.
