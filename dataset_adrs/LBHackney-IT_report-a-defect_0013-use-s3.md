# 13. Use AWS' S3 service for storing files

Date: 2019-11-21

## Status

Accepted

## Context

There is a user need to store evidence in the form of images, videos, and PDF
documents within the Report a Defect system.

This is a common need across Hackney projects and S3 is already in use across
the organisation. As such there is a project in flight to wrap S3 functionality
in an API that services can use.

At the time of writing, this API project is not ready nor is there an agreed
timeframe for when it will be ready.

There is no user need to be able to edit an image once uploaded, as such the S3
buckets will not need to have versioning enabled.

## Decision

Since there is an established pattern of using S3 for asset storage, we have
decided to continue this pattern and use S3 for this project.

We will be requesting that two buckets get made, one for the staging environment
and one for the production environment.

## Consequences

Using S3 now will make any future change to allow us to use the Hackney API
easier since the files shouldn't need to move. This will also allow the in-house
development team at Hackney to support the solution more easily.

S3 will allow us to use well established Rails tooling to handle file uploads
in a manner that is quick to iterate on.
