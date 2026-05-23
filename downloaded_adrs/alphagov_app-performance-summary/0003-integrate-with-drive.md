# 3. Integrate with google drive

Date: 2018-02-26

## Status

Accepted

## Context

- We're using [Google Data Studio](https://datastudio.google.com) to present KPIs to stakeholders.
- We're calculating application metrics on a periodic basis
- We need a way to get the data into a dashboard

## Decision

Integrate with google drive so we can load KPI reports into a spreadsheet within the GOV.UK team drive.

Use the [Pygsheets](http://pygsheets.readthedocs.io/) library for this.

The data in the sheet can then be used as a data source within data studio.

## Consequences

- We will need to manage another [service
  account](http://pygsheets.readthedocs.io/en/latest/authorizing.html)
- Some of our data infrastructure uses AWS, some of it uses google cloud
- Anyone on GOV.UK can view measures of application performance
