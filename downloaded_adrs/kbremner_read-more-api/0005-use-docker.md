# 5. Use Docker

Date: 2017-09-24

## Status

Accepted

## Context

Visual Studio 2017 added support for packaging applications using Docker and running them using Docker Compose.

## Decision

We will use Docker for packaging and running the application in a Linux container.

## Consequences

The application can be packaged to run on any platform that Docker supports.

The packaged application image can be run on any platform that supports running Docker Linux containers.

An additional container can be added to the default Docker Compose file to host the database and configure it's credentials. The Docker Compose file can then also be updated to supply the appropriate environment variables to the application container. This means that, when the application is run from Visual Studio, a database will be automatically created and the credentials will be passed to the application.

Docker for Windows uses Windows Hyper-V. This is only supported in Windows 10 Pro, meaning that that is the only version of Windows supported for building and running this project.
