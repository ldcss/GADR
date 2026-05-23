# 2. Store local copy of Syndication data

Date: 2017-06-07

## Status

Accepted

## Context

The [NHS's Syndicated Content](http://www.nhs.uk/aboutNHSChoices/professionals/syndication/Pages/Webservices.aspx)
holds information about GP surgeries.
Several of Connecting to Services applications need to make use of GP data, including the
[GP Finder](https://github.com/nhsuk/gp-finder) and [Profiles](https://github.com/nhsuk/profiles) projects.

The Syndication API is not intended for direct access in production environments.
The Syndication API returns data in XML, and information is spread across several subpages,
i.e. overview, services, facilities.

## Decision

The syndication XML API should be scraped nightly to create a local copy of the data.
What were multiple pages for a practice on the Syndication API will be merged into a single record per practice and
converted into the Connecting to Services teams preferred format, JSON.

## Consequences

A daily snapshot of relevant syndication data in JSON format is available for consumption by multiple applications,
enabling the whole dataset to be analysed and indexed.

The Syndication data will be scraped every night. This amounts to approximately 30,000 requests against the API over
the course of a 6 hour period.

Syndication will not queried in real time, insulating the application against failure of the Syndication API.
