# 3. Use Postcodes.io for postcode lookup

Date: 2017-06-14

## Status

Accepted

## Context

The application is about finding services closest to the search point. All
services have a co-ordinate in lat/lon format. Currently the application
requests either an out-code or a postcode as the search point. The submitted
postcode needs to be resolved to a lat/lon that can be used to query against.

## Decision

[Postcodes.io](https://postcodes.io/) provides both an out-code and a postcode
lookup. The results of which return latitude and longitude. The service is
free, [supported](https://postcodes.io/about),
[monitored](https://status.ideal-postcodes.co.uk/) and contains the full set of
active postcodes for the UK. Supplied by the
[ONS](https://data.gov.uk/dataset/national-statistics-postcode-lookup-uk).

## Consequences

Only currently active postcodes return responses. This means any
deactivated/deleted postcodes return 404s from which a co-ordinate can not be
retrieved and the application will not be able to return any results.
If additional search terms e.g. town names are added to the application an
additional lookup service might be required. That service might replace or be
used alongside Postcodes.io.
If the hosted service ever became unreliable or unavailable/shutdown the code,
data and [instructions](https://postcodes.io/docs) for how to run it is freely
available.
