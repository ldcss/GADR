---
layout: page
title: Contributing
---

## When to submit an ADR

The purpose of an Architectural Decision Record (ADR) is to record an
over-arching technical decision made by the development team in the
Archivematica  project. The development team consists of software developers,
archivists, and digital preservation specialists. An ADR is akin to a policy in
other contexts- it describes a way that future features or changes should be
implemented, rather than describing the features themselves (to submit a feature
idea, head to the [Issues repository]). Developers, analysts, and end-users will
use ADRs to understand how code was written and implementation decisions that
may be visible to the user.

Examples of situations when an ADR is appropriate:

* A change to how code is formatted
* Major architectural changes (e.g. bringing together or separation of
  components, upgrade of major dependencies, etc.)
* Deprecation of existing features

ADRs may be written retroactively to make a record of core features or
functionality.

## How to submit an ADR

ADRs must be submitted as a pull request to this repository. To get started,
first review currently accepted ADRs, then use the [template](template.md) to
write yours. As per [ADR-0000] the ADRs in this repository will use Markdown
Architectural Decision Record formatting.

ADRs must be submitted with the status “proposed" in the heading of the
template. An ADR can also be submitted as Work In Progress (WIP) if desired.

While ADRs are often technically focused, it’s good practice to write them in
plain, understandable language ([the Archivematica docs style guide] provides
good guidance on this subject).

When you submit an ADR be sure to assign at least one reviewer. If you’re
concerned about understandability you might include a reviewer of a different
background than your own (e.g. assign an analyst as a reviewer if you are a
developer and vice versa).

## How an ADR is reviewed and merged

The purpose for code review of an ADR is:

* clarity of language
* formatting
* ADR number collisions

Once the ADR is approved it can be merged by the submitter. While the code
review ensures understandability of the ADR, all Archivematica team and
community members are encouraged to participate in discussion about the proposed
changes.

## ADR statuses

After discussion and code review the ADR may be merged with the status accepted
(or rejected, or remain in proposed if deemed more appropriate). ADRs can also
be deprecated, or superseded by another ADR.

## Changes to the ADR process

To propose changes to ADR templates or these guidelines, file an issue in the
Archivematica Issues repo.

## More information

More information on Markdown Architectural Decision Records (MADR) is available
at [adr.github.io/madr](https://adr.github.io/madr/). General information about
architectural decision records is available at
[adr.github.io](https://adr.github.io/).

[Issues repository]: https://github.com/archivematica/Issues
[ADR-0000]: 0000-use-markdown-architectural-decision-records.md
[the Archivematica docs style guide]: https://github.com/artefactual/archivematica-docs/blob/HEAD/style_guide.md
