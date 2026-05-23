# 5 Utility Context Lazily Initialized

## Status

Proposed 2017-12-07

Accepted 2017-12-07

mentions [1](1-ADR_directory_identified_by_marker_file.md)

## Context

The [synchronous utils](../../src/adr_util_sync.js) are intended to be used by commands to work on ADRs, with the given context of the project, e.g. the [adr marker file](1-ADR_directory_identified_by_marker_file.md).  
Since the context is mandatory (the ADR directory, existing ADRs), it is initialized at the beginning, in the object's constructor.

Several commands (scripts) already include that script, and initialize the object on the script loading, as part of the `require` statement.  
This resulted in loading the context whenever a command is loaded.  

This might have performance implications, but the more immediate functional lacuna is that this then assumes that the context *can* be loaded every time.  
Of course, this assumption breaks - when running the `init` command, where by definition there is no context to load - the `init` command creates that.

This resulted in trying to run the `init` command, on an existing directory, in an error.

## Decision
The ADR project context will be loaded lazily, only when needed.  
This assumes the `init` command doesn't require it, and hence will not invoke any commands that require that context (e.g. the existing files).  
So any command that is loaded can still create the context object and create an instance of, but the actual context will be loaded easily.

This assumption seems safe enough since `init` command indeed creates the context (the `.adr` file).  
And this will probably hold for similar commands.  
Commands that will require the ADR context, will continue to use it as today, and it will be loaded lazily.

We need of course to make sure that the context isn't created/calculated every time it is called; e.g. searching for the ADR dir every time one of the utility functions is called. In other words - memoize the context-creating functions.

## Consequences
ADR context will be created when necessary, and cached to be used throughout the command execution.


    