# OAI-PMH harvests for Dome-based Ingests

## Context

Some of the target collections are already present in Dome, and it is simpler
to use Dome as the ingest source than upstream systems. Further, as Dome supports
OAI-PMH and OAI-ORE, these interfaces could be used to retrieve  
relevant information, such as the bitstreams of digital assets, directly from Dome. 

To accomplish this, a custom ingest script or a third-party tool could be used for this purpose. 
Such a tool is available for TIMDEX related ingests [link]() and could be modified for ingesting
digital assets to DOS.

## Decision

Ingest will be handled through the existing OAI-PMH/ORE tool in conjunction with scripts written to prepare that output for the DOS API.


## Status

Accepted

## Consequences

1. Integration tests should be created and automated testing should be performed to ensure that the scripts
run properly against the DOS API.  

2. Alternate ingest scripts will still need to be created for sources that don't support OAI.