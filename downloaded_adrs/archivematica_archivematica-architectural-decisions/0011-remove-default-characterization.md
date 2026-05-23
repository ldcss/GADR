---
layout: page
adr: "0011"
title: Removal of default characterization rule
status: accepted
deciders: Sarah Romkey
date: 2024-08-27
---

## Context and problem statement

Archivematica is installed with default rules and commands for various
preservation actions,including characterization, which can be altered by an
administrator through the Format Policy Registry (FPR). In most cases, rules are
set to run according to which format is ingested, but in the case of
characterization, there has been a default, or a "fall back" rule, which is to
run [FITS](https://projects.iq.harvard.edu/fits) if a more specific rule for
that format doesn't exist. This ADR proposes to remove that default rule so that
characterization is treated like other preservation actions.

## Decision drivers

* The primary decision driver is the maintenance of FITS itself and the lack of
  a suitable replacement. FITS is a Java application and running it in a secure
  way in the Archivematica environment has been a challenge.
* Due to performance issues with FITS, it has been Artefactual System's
  recommendation on installation to have the command disabled for some time now.
  Therefore many Archivematica users are already not using FITS.
* We have found that the approach of throwing a large, generalist tool at files
  and see "what sticks" has not been the most useful approach. In short, it
  results in a large quantity of metadata written to the AIP METS files which is
  of limited utility
  (see [Issue 703](https://github.com/archivematica/Issues/issues/703)for
  discussion.)
* Our primary concern in the FPR now is to make it more maintainable and
  understandable. We are working toward a future state where changing rules,
  adding tools, changing commands, etc, is easier and therefore users will be
  better able to customize the FPR locally.
* While the universe of open source digital preservation tools is expansive,
  from consulting [COPTR](https://coptr.digipres.org/index.php/Tool_Functions)
  there doesn't appear to be a clear replacement for FITS.
  [Metadata extraction](https://coptr.digipres.org/index.php/Metadata_Extraction)
  appears to be the closest equivalent to characterization and most of the tools
  listed are best suited to specific file types. As per the point above, the
  intention should be that Archivematica users are more easily able to install
  and use these tools into the FPR should they so choose. This includes choosing
  an alternate default characterization tool on a per-institution basis, which
  is possible by altering the Default Characterization Rule in the FPR.

## Considered options

* Remove FITS from Archivematica codebase and do not replace
* Remove FITS from Archivematica codebase and replace with a different
  generalist characterization tool
* Maintain the status quo

## Decision outcome

FITS was removed in Archivematica 1.17, released December 6, 2024. Related
pull requests can be found attached to
[Issue 703](https://github.com/archivematica/Issues/issues/703).

## Links <!-- optional -->
