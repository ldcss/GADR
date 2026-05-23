# 8. Use Snyk to scan for CVEs

Date: 2020-11-20

## Status

Accepted

## Context

We want to be aware of CVEs (Common Vulnerabilities and Exposures) before they
end up in production, and make sure to block deployments with known high
severity CVEs. Snyk allows us to scan our PRs for CVEs and fail builds if there
are any vulnerabilities in the code we've written.

## Decision

We will use Snyk to:

- Run scans on PRs provide results and fail builds if any known high severity
  CVEs are found.
- Run scans on main and fail builds on high severity CVEs, posting the results
  to the Snyk platform for monitoring.
- Run nightly scans on the docker image and app dependencies.

## Consequences

We will know of any CVEs present in the codebase before they get to production
and ensure that our app is as secure as possible.
