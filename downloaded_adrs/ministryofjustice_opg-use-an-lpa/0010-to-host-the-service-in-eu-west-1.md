# 10. To host the service in eu-west-1

Date: 2019-05-01

## Status

Accepted

## Context

We've received the following guidance from the MOJ:
```
The MOJ does not by default or routine require ‘UK only hosting’ or ‘UK only services’ for data privacy, 
data protection or information security reasons.
```
and
```
The MOJ has no plans to inshore data (i.e. limiting and / or returning data to the UK) for privacy or security 
reasons, nor is the MOJ asking its partners (for example, commercial suppliers) to do so.
```

Full details here: [MOJ data sovereignty questions](https://ministryofjustice.github.io/security-guidance/mythbusting/data-sovereignty/#data-sovereignty-questions)

## Decision

Use an LPA's infrastructure will be based in eu-west-1; thus not in the alternative, eu-west-2.

## Consequences

* Use an LPA's infrastructure will be in the same region as all other OPG services.
* AWS services in eu-west-1 are typically cheaper than eu-west-2.
* New services and features are typically released earlier in eu-west-1.
