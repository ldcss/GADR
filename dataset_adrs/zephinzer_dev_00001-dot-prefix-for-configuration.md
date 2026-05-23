# Use dot prefix for configuration files

This ADR records the decision to standardise the configuration file path and location by standardising the configuration files as detectable using the regular expressions: `.dev(\.[a-zA-Z\-\_]+)?.yaml` in both the user home directory and the current working directory.

## Status

Currently to facilitate extensibility, two locations are searched for:

1. `~/dev.yaml`
2. `./dev.yaml`

Additionally, there exists an `includes` property which allows for each file to include other files.

## Context

1. The current implementation goes against a convention where global configuration files are prefixed with a period
2. I want to be able to do writebacks to the configuration, an exact example would be `dev add repo ${REPO_URL}`, and the current implementation makes it messy because the configuration files can be anywhere.

## Decision

I have made the decision for configuration files to look like: `\.dev(\.[a-zA-Z\-\_\.]+)?\.yaml` and for the application to only search in the user home directory and current working directory. The `includes` property will be removed.

## Consequences

This possibly reduces some extensibility by removing the possibility for custom inclusions. As with all constraints however, comes the benefit of standards and `dev` configurations will be immediately recognisable from it's filename as a configuration file (from the prefixed period, hopefully?).
