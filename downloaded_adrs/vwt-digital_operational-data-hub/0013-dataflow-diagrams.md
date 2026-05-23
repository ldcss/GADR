# 12. Dataflow Diagrams

Date: 2021-06-01

## Status

Accepted

## Context

We feel the need to define that every config folder should contain at least one dataflow diagram.

## Decision

We decided that every config folder should contain at least one dataflow diagram.

### Dataflow Diagram

Every config with a cloudbuild should contain a dataflow diagram. This diagram contains the dataflow of the GCP project the config is for. It is also possible to have multiple diagrams if there are multiple dataflows. [Here](https://github.com/vwt-digital-config/snb-link2-int-config/tree/develop/dataflow_information/tmob_emails_link2) and [here](https://github.com/vwt-digital-config/snb-tmob-problm-int-config/tree/develop/dataflow_information/tmob_emails_link2) examples of dataflow diagrams can be found.

The diagrams are made via the python package [diagrams](https://github.com/mingrammer/diagrams).

## Consequences
