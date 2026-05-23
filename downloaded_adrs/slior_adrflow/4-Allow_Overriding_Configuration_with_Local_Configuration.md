# 4 Allow Overriding Configuration with Local Configuration

## Status

Proposed 2017-08-08
  
Accepted 2017-08-08

mentions 1

## Context

The ADR flow tool is a command line tool for managing ADR files. It is aimed to be used in command line, in MS-Windows primarily, but also other platforms.

As a guiding principle, and in order to preserve simplicity, we don't want to introduce a separate data store. Data is stored and managed in files. This includes configuration, which should be explicit and easily identifiable and editable.

Given this, in [ADR 1](1-ADR_directory_identified_by_marker_file.md), we decided that the ADR directory is identified by a file called `.adr`. This file will also contain configuration of the tool. This is to reduce the number of moving parts; so the marker file (`.adr`) is used also as a configuration file.  

Part of the value statement is for these files to be available in source control, and easily shared and collaborated on by a team. This means the marker file needs to be version-controlled as well.  

At the same time, the configuration may change on a per-developer basis. For example, the location of the editor used to edit ADRs.

### Alternative 1: Introduce a Separate Configuration File
This means that we, by definition, and always will have a separate configuraton file, on top of an empty marker file.
This makes sharing configuration slightly harder, and makes it hard to share some of the configuration and customize others.

### Alternative 2: Use Environment Variables
With this approach we configure the system using environment variables.
This is OS-dependenet, and makes the configuration somewhat less explicit. It's also harder to share across a team where necessary.

## Decision
We will keep the `.adr` file, with its current dual role - a marker file, and a *shared* configuration file.  

In addition, we'll add the option to supply a `local.adr` file, with the same format as the `.adr` file, and allow a developer to specify properties to override there.

Properties that are specified only in `.adr` will have their values taken from there.

## Consequences

Developers will need to specify a separate `local.adr` file for local configuration (overriding `.adr`).

In order to avoid overriding each other's configuration, the `local.adr` will need to ignored by the version control system used, e.g. added to `.gitignore` if git is used.

    