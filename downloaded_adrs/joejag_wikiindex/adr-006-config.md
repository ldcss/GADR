# Config

## Context

* We need to set the port and other config values for our application
* We do not know the deployment environment yet

## Decisions

* We will use environment variables to configure the app, rather than a file

## Alternatives Considered

* A YAML file would allow for structured config