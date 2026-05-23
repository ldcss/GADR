# 10. Packaging Node Exporter as .deb for Verify

Date: 2018-08-15

## Status

Accepted

## Context

Node Exporter needs to be installed on Verify's infrastructure so that machine metrics can be gathered.
Verify runs Ubuntu Trusty which does not have an existing node exporter package.
Verify has an existing workflow for packaging binaries which can be leveraged to package node exporter. 
## Decision

Node exporter will be packaged as a deb using FPM following Verify's exiting packaging workflow.

## Consequences

The use of Verify's infrastructure ties the Node exporter package to Verify, the node exporter would need to be repackaged for other programs to be able to be used.
