# 12. Feed Parsing Dependencies

Date: 2020-10-29

## Status

Accepted

## Context

During the parsing of different feeds it has become clear that some feed files contain partial information related to Positions, Transactions and Tickers (think DBS, BOS, Credit Suisse) which end up creating inconsistent and incomplete PriveXML/JSON result files with partial information which if handled in CDH will break decision made in [0002 CDH ETL Logic Boundaries](./0002-cdh-etl-logic-boundaries.md).

From existing processing of feed files, such inconsistency is resolved by reviewing previous results based on time ranges back into the past which allows us reconcile such inconsistencies, by creating a clear picture due to information on Tickers, Positions and Transactions as required.  

## Solutions Considered

1. Reprocess source feed files
This will allow parsers to implement necessary branch logic which when inconsistencies such as described occurs, will retrieve data feed source files for a giving time range (t-1, t-2, t-4,...etc) which will be then used to reconcile inconsistencies.

Benefits:
 - Each parser is self contained and can reprocess previously existing data feed source files to reconcile it's own intricacies
 - Each parsers logic is self contained and the outside world as no concept of what processes is used for generating the final outcome.

Problems:
 - Each parser falling into such use case will escalate processing of a batch to process more files per requests.
 - Increased processing time for processing a batch of files due to the need to reprocess (clean, parse, normalize) feed data.
 - We must scale vertically as needed to meet resource requirements for constraints of reprocessing more files per feed request (if necessary only).

2. Reuse previous parsing results

Since previous feed files were already processed to create their corresponding PriveXML/JSON which contains the cleaned and normalized results of such a batch of feed files for each time range (t-1, t-2,..., etc). If these are stored within an appropriate store (S3, MySQL, Redis) which will allow immediate access as such result do not change, then we can skip reprocessing of the original source files and use this as the source of the reconciliation processing during feed parsing of new feed batches.

Benefits:
 - Each parser still only ever processing the provided batch (same memory and cpu usage)
 - Reprocessing of source files only ever occurs when such result does not yet exists (saving cpu cycles per feed)
 - Each parser retrieves previous results based on specific critierais with a single query to retrive as many t-n time range.

Problems:
 - If relation database table is used then we create a shared resource across horizontal scaling of ETL service. 
     (We can mitigate this by using a scalable store (e.g s3) that can handle as much request for files as needed).
 - We must implement more code to provide cleaner abstractions for retrieving/querying previous results (setup cost)
 - We must still fall back to processing source files if the result does not yet exists in db (so why not do it all the time?).

**TradeOffs: Performance over Code Complexity**

Because if we choose option 1 then we increase complexity in execution time as each parsing data can requests multiple files for reprocessing to reconcile inconsistency, while option 2 means we must manage another database if going on a relational store to persist such processing results for later read-heavy querying.


## Decision

We chosen to following the solution prescribed in Option 2, using a relation database table to store records to such PriveXML/JSON results which will be based on processing date and feed category for later retrieval. This can be stored as blobbed or have the contents stored externally (on S3) where the table maintains necessary pointers to location for retrieval through a library.

## Consequences

Implement new relation data table necessary to manage such query results and create a central library for retrieval of such as required for parsing processing or later-processing.

