# Use Architectural Decision Records

* Date: 2018-19-06

## Context and Problem Statement

I want to retrace why a certain development tool has been placed into this project.

## Considered Options

* do not document decision explicitly
* use commit messages + changelog for documentation purposes
* extend README.md with rationale + background information
* use [Lightweight architecutral decision records](#lightweight_architectural_decision_records)

## Choosen option

Lightweight architecutral decision records using an template adapted from [madr](https://adr.github.io/madr/)

**Reasons**

I decided to include ladrs as a recommended practice, because:

* they provide an easily accessible and well defined format for documenting information about the presence of concepts / dependencies / tools used in a project
* they provide background information, documentation and rationale that help onboarding
* they are easily editable without additional documentation tools and can be updated and versioned through git

**Notes**

* an up-to-date template file has been added to the project
* keep core reason to a sizable number (<= 3), add **tldr;** section if more are necessary / helpful
* there is no additional tooling recommended at this point, as:
  - the ladr format as is is lighweight enough already and can be managed without additional tooling
  - dealing with plain markdown files can easily done by anyone using copy / paste, whereas additional tooling will require developers memorizing new commands
* [madr](https://adr.github.io/madr/) has been applied as a base template, as:
  - make access to creating and reading up on decision easier
  - adaptions made:
    - the section `Pros and Cons of the Options` has been replaced in favor of `Background information`
    - the section `Decision outcome`has been replaced in favor of `Choosen option`

## Background information

### Lightweight architecteural decision records

Background information:

* https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records
* https://github.com/joelparkerhenderson/architecture_decision_record

Considered Tools:
* https://adr.github.io/madr/
* https://github.com/npryce/adr-tools
