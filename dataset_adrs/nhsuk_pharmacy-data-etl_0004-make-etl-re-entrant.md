# 4. Make ETL re-entrant

Date: 2017-06-15

## Status

Accepted

## Context

If the ETL if is interrupted it will need to start over again, i.e. a 6 hour ETL is stopped in the 5th hour, restarting will take another 6 hours to finish.

## Decision

The ETL will be re-entrant, storing state on a regular basis.
Restarting the ETL will pick up from the last point.

## Consequences

When running the ETL locally the process can be stopped and started without losing progress.
Additional complexity added to the code to maintain state, and clear state if the ETL should start afresh.
