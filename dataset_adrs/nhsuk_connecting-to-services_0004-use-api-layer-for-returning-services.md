# 4. Use API layer for returning services

Date: 2017-06-14

## Status

Accepted

## Context

The service data had been stored in a flat file and with the use of a number of
libraries [geolib](https://www.npmjs.com/package/geolib),
[ngeohash](https://www.npmjs.com/package/ngeohash) and
[geo-nearby](https://www.npmjs.com/package/geo-nearby) the capabilities of a
geo-location search was added. However, this is a CPU intense operation. Node
is not best suited to that use case. This resulted in the Node process being
blocked for the duration of the calculation. The performance of the site wasn't
affected too much when services (that were open) were found close to the search
point. However, when a lot of results were returned (when searches originated
within highly populated areas) and there were no services open the processing
took a considerable amount of time (several minutes). This resulted in the web
site becoming unable to serve requests to new users.

## Decision

It was decided to move the processing of the geo-location search to a separate
application so the web site would continue to serve pages to new users.

## Consequences

Running the CPU intensive operations in a separate container means the
processing capacity is easily scaled up by simply adding additional containers.
With the searches being done in the API the implementation of that search is
able to be changed without requiring changes to the website. This application
become just concerned with serving web pages as best it can.
