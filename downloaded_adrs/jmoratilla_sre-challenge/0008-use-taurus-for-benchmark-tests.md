# 8. use taurus for benchmark tests

Date: 2020-05-25

## Status

Accepted

## Context

To perform benchmarking tests, I want to set some resources capable to generate
 a high volume of requests against the cluster.

To do this, I could use several tools, like JMeter, Garret, or Taurus.

But I like Blazemeter's Taurus over all because it is very simple to setup and
execute tests.

With Taurus you can create JMeter tests, or use other tools like Selenium, in 
 order to execute and collect results.

Then It generates a report that can be easily imported in a JMeter tool or
 open it in a data analysis tool like jupyter notebook to draw new diagrams.


## Decision

Create an instance with an easy test (Just request the keys and the metrics).


## Consequences

