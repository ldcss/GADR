# TUS Protocol for Resumable Uploads

## Context
The storage service needs a function for uploading files both large and small. It also needs to be able to handle interruptions that can occurr while uploading data.

While searching for a solution it became clear that AspNetCore does have basic uploading capabilites in which files can be uploaded using an `IFormFile` that is bound to a model. This is problematic because the file is completely buffered in memory or on disk which makes this solution not ideal for large files and high frequency uploads.

Taken from [Microsoft's File Uploading Documentation](https://docs.microsoft.com/en-us/aspnet/core/mvc/models/file-uploads#file-upload-scenarios):
> Any single buffered file exceeding 64KB will be moved from RAM to a temp file on disk on the server. The resources (disk, RAM) used by file uploads depend on the number and size of concurrent file uploads. Streaming isn't so much about perf, it's about scale. If you try to buffer too many uploads, your site will crash when it runs out of memory or disk space.

When uploading large files AspNetCore doesn't provide any form of resilience (as of version 3.1). If a network connection is dropped the client if forced to restart the upload from the beginning. As files take longer to upload there is an increasing chance for the connection to be interrupted. File validation occurrs after the upload process is complete. If the file is corrupted then the file will need to be re-uploaded.

## Decision
We will use the `tusdotnet` for our TUS protocol implementation.

We will integrate the Identity Service with `tusdotnet`.

We will implement a proof of concept custom storage container for `tusdotnet` that connects to Azure Blob Storage.

## Status
Accepted

## Consequences
There are a number of cons to using the TUS protocol:
1. `tusdotnet` could become abandonware which would require us to maintain the implementation.
2. Microsoft does not supported the TUS protocol natively in .NET

In addition there are far more pros to use the TUS protocol:
1. It is HTTP based
2. Works in unreliable network conditions
3. Handles large files and long uploads
4. Has built in pausing and resuming
5. Not based off proprietary solutions

Some notes about the TUS protocol:
1. The TUS protocol requires the use of custom headers.
2. The TUS protocol's custom headers are not prefixed with `X-` because:
    > The “X-“ prefix for headers has been deprecated, see [RFC 6648](http://tools.ietf.org/html/rfc6648).