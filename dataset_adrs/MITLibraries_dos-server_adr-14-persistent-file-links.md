# Handles for Generation of Persistent Links to Bitstreams

## Context

DOS returns internally generated unique identifiers for files it ingests.

The URLs are roughly of the form (at the time of this ADR, plain integer identifiers are returned):

https://dos-stage.mitlib.net/file?id=123e4567-e89b-12d3-a456-556642440000

Once files are ingested, the identifiers are stored in ArchivesSpace.

This may result in a situation where if URLs to files need to change (e.g., if 
the AWS bucket name for DOS changes), all links in ArchivesSpace need to be updated for
all ingested files.

Although DOS can be made to generate persistent identifies, it is desirable to externalize 
this functionality for reuse and portability considerations. 
The Handle System can be used for this purpose. Handles are already being used in 
Dome and DSpace, and there is organizational familiarity with the system. 

## Decision

Handle System will be used to generate persistent links. DOS will use the 
Handle server API to generate handles. Handles will be returned when the 
relevant DOS end point is invoked.

## Status

Accepted

## Consequences

The handle sever will be different from the one used by (and embedded in) Dome (and DSpace). Dome handles
point to web pages in Dome, whereas DOS handles will point to digital files/bitstreams. 

URLs returned by DOS will be roughly of the form:

https://handles.mit.edu/1721.6/176472

Internally, the handle server will contain the mapping 
(e.g., from https://handles.mit.edu/1721.6/176472 to https://dos-stage.mitlib.net/file?id=123e4567-e89b-12d3-a456-556642440000).