# 19. Store data validation rules in JSON files

Date: 2018-08-28

## Status

Accepted

## Context

Each framework has a specific description of what data must be submitted in the
monthly MI return. This description outlines what fields should be submitted,
what data types are accepted and any validation rules which should be applied.

At the moment, these rules are encapsulated in the Excel template which
suppliers download, using drop-downs, tool-tips and sometimes macros.

A separate copy of these rules is configured for each framework in MISO, which
the service uses to validate templates have been filed in correctly when
uploaded.

### Longer term approach

In future, we want a single source for the rules for framework data submissions
which we can use for various tasks including:
- generating submission templates in different formats (eg Excel, ODS, CSV)
- validating submitted returns
- documenting any APIs

These rules should ideally be stored in a central place and made available to
any services which require them via an API. This will allow new services to
share the ruleset and description.

The high-level principle is that there should be an artefact that describes the
rules that need to be applied.

The artefacts need to be version controlled so they can be changed during the
lifetime of the framework. Services may need to access and used outdated
versions of the rules.


### Interim approach

For the initial waves of on-boarding, we expect only a small number of
frameworks to be submitting monthly returns.

While we develop our approach, and learn more about the varied rules for each
framework, we will use an interim approach for storing the rules.

We will create a JSON file for each framework which outlines the data structure
required and the validation rules for each field. This JSON file will be stored
in a GitHub repository, and used to generate templates and validate submitted
files.

Eventually, we will develop an API to provide access to this information.

## Decision

We will create a JSON file for each framework and store it in a GitHub
repository.

This JSON file will describe each field, it's data type and associated
validation rules.

We will migrate these files to a longer-term solution once we have a better
understanding of the required rules for each framework.

## Consequences

We will produce a file for each framework that we migrate to the Data Submission
Service, but will need to replace this late.
