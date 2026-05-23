# 2. Use CSV rather than JSON for allowed user list

Date: 2019-11-12

## Status

Accepted

## Context

Using a JSON file for the `allowed-users` listing makes the code within the
application straight forward and ofc, the default data format within a JS app
should be JSON (controversial). However, managing the file is (at least atm)
being done by a human. Editing a JSON file and ensuring it is valid JSON is
more challenging than a CSV file. If the file is malformed the application is
unavailable, therefore, reducing this risk is paramount.

## Decision

The decision is to use a CSV format for the listing of allowed users.

## Consequences

The consequence of using a CSV formatted file include:
* the code is a little more involved even without introducing a third party
  library (which hasn't been done)
* the risk of a malformed file is greatly reduced
* the ability for humans to manage the contents of the file and be comfortable
  with making changes to it greatly increases
