# 6. Use in-house postcodes search rather than postcodes.io

Date: 2019-01-07

## Status

Accepted

## Context

The application has been using https://postcodes.io/. Postcodes.io is available
for free and does not require any relationship between consumer and supplier.
One of the drawbacks to this is that although support is available when using
the free tier, there is no provision for any specific support relationship.
More formal relationships are available but this is through the paid product
https://ideal-postcodes.co.uk/.  Given the number of requests and the fact the
free tier was supplying the information required, it had previously been
decided there was no need to migrate to a paid product. However, the strategic
direction has been set such that high value APIs, usable across many products
should be supplied in-house. To that end, there is now an in-house postcode
search available. 

## Decision

The decision is to replace the use of postcodes.io with the in-house postcode
lookup, as per the strategic direction.

## Consequences

The consequences of switching to the in-house API include:
* Updating the application for the different response model
* A change to the application messaging for non-English, UK postcodes. This is
  due to the in-house search including only English postcodes, whereas
  postcodes.io maintains UK postcodes
