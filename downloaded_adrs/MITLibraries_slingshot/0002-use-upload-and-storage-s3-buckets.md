# 2. Use upload and storage S3 buckets

Date: 2019-06-07

## Status

Accepted

## Context

Some sort of minimal storage and workflow system needs to be built for publishing GIS data layers. It doesn't make sense to spend more effort on this than necessary since it's a problem that ultimately should be solved for the more general case. In the absence of such a system, this tool will support the existing process in a cloud native manner.

With the current process, GIS analysts place zipfiles containing both data and metadata in a specific folder on a shared network drive. An automated script runs weekly to make any new layers available in GeoWeb. Publishing requires both extracting the zipfile to a new location and processing the data.

## Decision

Use a bucket for uploaded zipfiles and a bucket for the extracted zipfiles. The uploaded zipfiles will not be removed once processed.

## Consequences

The publishing process will need to have a method for keeping the two buckets in sync. Either the GIS analysts will need training and access to the upload bucket or a minimal web interface will need to be put in front of it.
