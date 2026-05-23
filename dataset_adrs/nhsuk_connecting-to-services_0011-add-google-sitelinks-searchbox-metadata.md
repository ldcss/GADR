# 11. Add Google Sitelinks Searchbox Metadata

Date: 2018-01-23

## Status

Superceded by [13. Remove Google Sitelinks Searchbox Metadata](0013-remove-google-sitelinks-searchbox-metadata.md)

## Context

Metadata can be added to a web site's home page to enable a search box directly within Google.

## Decision

Adding the required metadata is straight forward as the sites' search URL is the correct format for the Sitelinks Searchbox.
An additional term will be added to the query string to allow analytic metrics to distinguish Google searches from searches initiated from the main site.

## Consequences

Some searches will originate from Google, reducing the number of searches originating from the Pharmacy Finder's search page.
