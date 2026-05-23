# 1 ADR directory identified by marker file

## Status

Proposed 2017-07-01  
Accepted 2017-07-11

## Context

The ADR utility is meant to be run inside a project, and initialize the ADR management in that project's file system.  
We would like to rely only on the project's file system, and make it versionable in traditional version control tools, e.g. git.  

To this end, all scripts in this utility must rely solely on the file system to find the correct location of the ADR files and relevant configurations.  
In order not to rely on some environment setting, we decided to opt for a special marker file, named specifically `.adr`, that will mark the location of the ADRs.

Other options include to have an environment variable, rely on a naming convention, or specify it in a configuration in the root.  
The option of the marker file seems safest and at the same time simplest, with the least number of assumptions or conventions made by the user.

The downside is of course that moving the file will potentially lead to malfunctioning scripts.  
At the same time, moving the marker file, with the ADRs to a new place is easy - just move the files.

The only remaining assumption is that the ADR utility with a working directory that is a parent of the ADR. This is usually not a problem if the user is working on a specific project.

## Decision

The `init` command will create the marker `.adr` file which will be used to identify the ADR directory.

In addition, this file will be a simple properties file which will maintain other program configuration, and allows users to modify it for different features; e.g. configuration an editor.

## Consequences

See above:
1. The ADR utility must be invoked in some ancestor directory of the ADR directory.
2. Loss of this file will prevent the ADR directory from working properly
3. The configuration of the ADR will be part of the versioned sources.
   This might prevent different users from having different configurations easily (can be worked around by changing it locally and not committing this file)/
