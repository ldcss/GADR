---
layout: page
status: accepted
adr: "0005"
title: New API endpoint for CSV validation
deciders:
date: 2018-03-28
---

## Context and problem statement

Archivematica users rely on spreadsheets created in a specific way to
perform tasks within or after Archivematica. Documentations and
examples can be found in the [Import
metadata](https://www.archivematica.org/en/docs/archivematica-1.9/user-manual/transfer/import-metadata/)
section but there is no clear validation as can be performed by a
machine. As one example, the metadata.csv and rights.csv files are
"special" and are utilized by Archivematica to add metadata or rights
metadata into the AIP's METS file.  Another example is the Avalon
Media System having a specific Manifest.csv file that is used to
recreate hierarchical information and additional metadata, which is
used after a DIP is created from a stored AIP. It would be beneficial
if this manifest could be validated prior to going through the
preservation process.  Both of these examples would benefit from a
validation service that a user (or automated system) could access
prior to ingest into Archivematica.

## Decision drivers

* More closely integrate two open source projects: Archivematica and Avalon
* [Feature request](https://github.com/archivematica/Issues/issues/563) for
  validation of Archivematica-specific CSVs within Archivematica
* Creation of something for a specific purpose that can later be extended to
  suit many use cases

## Considered options

1. API endpoint for pre-ingest CSV validation
2. Create validation microservice
3. Using Automation-tools to validate specific CSVs
4. Upload UI for validating CSV files

## Decision outcome

Chosen option: "1. API endpoint for pre-ingest CSV validation", because it is
flexible, it lays the groundwork for future work around CSV validation as a step
to be taken by Archivematica. It doesn't have the complications of the long-term
maintenance and testing of a GUI component. It can be more easily automated. The
solution allows for custom or institutionally-specific CSV to be used/added.

Technically, this would live in the Archivematica codebase and be a new endpoint
in the [Archivematica API](https://wiki.archivematica.org/Archivematica_API)

Proposed endpoint below:

```yaml
URL: /api/transfer/validate_csv
Verb: POST
Validates local CSV with validator service Python script
Parameters: CSV
    input: Path to the CSV
    validator: Name of service CSV should be checked against, i.e. "avalon"
                or "rights"
Response: JSON
    message: Approval or non-approval, depending on service output
```

### Positive consequences

* Fulfills requirement of Avalon/Archivematica integration work.
* Relatively small feature with big potential benefits.
* Lays foundation for more development in the future.

### Negative consequences

* Code must be maintained and tested over time.
* User would need API expertise to benefit from this feature.
* Implementation -- timeouts on very big CSVs?

## Pros and cons of the options

Options are discussed with pros/cons outlined in the linked issue and pull
request. Some are implicit in the above decision outcome and positive/negative
consequences sections.

## Links

* [Issue #563, "Problem: It is difficult to validate rights.csv and metadata.csv before ingest"](https://github.com/archivematica/Issues/issues/563)
* [Automation-tools PR #98, Add script for validating Avalon Media System manifest CSV](https://github.com/artefactual/automation-tools/pull/98)
