# Design document for linking workspace data to samples

## Document purpose

Provide one or more design options for linking data in the KBase Workspace Service to
samples stored in the KBase Sample Service.

## Definitions

* SS - Sample Service
* WSS - Workspace Service
* RE - Relation Engine

## General design considerations

* A user having access to a sample **does not** mean they necessarily have access to data linked
  to that sample. They must have explicit workspace permissions for the data.
* A user having access to data linked to a sample **does** have access to the sample.
* When creating a new version of a sample, data links are not automatically updated.
  * This could be a feature in the future, either automatically or on request.
* Data can only be linked to a single sample.
  * Although it can be linked to multiple versions of the same sample.

## Options

### Links are managed by the SS / Relation Engine

* Link requests go to the SS, which
    * Checks that the user has explicit access to the sample and the WSS data.
    * Creates a link from the RE WSS shadow object representing the data to a node in the sample.
* Metadata about the link could be stored in the RE DB, such as denoting a column in the data
  object that is linked to the sample, rather than the entire data object.
* RE graph traversals can be used to find samples from linked data and vice versa.

#### Implications

* Data copies are not linked to the Sample.
* The WSS knows nothing about data <-> sample linkages.

### Links are managed by WSS Data types

* An `@sample` (or something) annotation is added to the WSS. When the WSS typechecks a data
  object containing the annotation, it looks up the sample in the SS and ensures the user has
  explicit access to the sample.
* If RE queries from data <-> sample are required, the RE indexer would need to be updated
  to add appropriate links for each data type with the `@sample` annotation.
* When requesting a sample via linked data, the SS will need to check that the data in the WSS
  contains an appropriate link to the sample.

#### Implications
* Every sample associated data type needs to be updated to contain at least one `@sample`
  annotation.
* Data types with columns, etc. may require many annotations, which could severely slow down
  saves.
* The data will continue to be linked to the sample on a copy.
* A new version of data must be saved to add or update links.

## Decision

On 2020/1/28, the decision was made to go with option 1 by the KBase APS Samples group.
