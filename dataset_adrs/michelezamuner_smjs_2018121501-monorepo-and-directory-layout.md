# Monorepo and directory layout


## Context

Following from decision [2018120802](2018120802-implement-clean-architecture.md), we want to follow the tenet of [screaming architecture](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html), stating that the first level directories of the application's source tree should represent the use cases, or features, of the application.

However, we cannot define domain modules inside application directories, because the domain cannot be mapped 1-to-1 to application features, since the domain is independent from the application. In practical terms, this means that it could happen that two different features will need the same domain module, and if this domain module is defined in feature `A`, and feature `B` requires those domain concepts as well, then feature `B` will have to know about feature `A`, even if this makes no sense as far as the semantic of those features are concerned.

Additionally, we cannot define adapters, or "infrastructure" code, inside feature directories either, because application cannot know about adapters, and very often an adapter targets multiple features, like a Web adapter can target different features of a primary port, and even a secondary adapter could be the target of different features, if it acts like a mediator, for example with commands or events.

We're currently using only one source code repository, and we don't want to go through the hassle of maintaining multiple repositories yet, because the project structure is still being actively changed. On top of that, we want to support a plugin architecture, where multiple different kinds of applications can be built by assembling together plugins. This is exactly the purpose of Clean Architecture, with maybe the only difference that the typical example of Clean Architecture is a Web application where there's only one application supporting different features, while we'll have different applications that can possibly be built from the same components: this, however, is just a deploying detail.


## Decision

To avoid dealing with multiple source code repositories, we'll use the "monorepo" approach, meaning keeping everything inside a single source code repository.

As far as the directory structure is concerned, this project is a bit unusual, since many different applications we'll be built from it, by assembling different plugins, instead of having only one possible application. This means that we cannot really display the application use cases at the first level of the directory tree, because there all applications and plugins will be located instead:
```
sloth-machine-framework
    domain
        smf
sloth-machine-architecture
    domain
        sma
virtual-machine
    application
        vm
architecture-loader
    application
        arcl
program-loader
    application
        pl
local-architecture-loader
    adapters
        larcl
file-program-loader
    adapters
        fpl
sloth-machine
    adapters
        sm
    -> sloth-machine-framework
    -> sloth-machine-architecture
    -> virtual-machine
    -> architecture-loader
    -> program-loader
    -> local-architecture-loader
    -> file-program-loader
...
```

We can argue that this directory layout is still quite "screaming", because it's displaying the features of our application, or we should better say "toolkit" since there are multiple applications: virtual machine, assemblers, compilers, debuggers, etc. This should state very clearly what's the purpose of these systems.

It's interesting to point out, additionally, that here we have two different kinds of plugins: to the first one belong the plugins that are added during development of the application, because they're necessary for its structure, like `sloth_machine_core`, or all the `feature` ones; the second kind of plugins, instead, contains all the "mods" that can be added to an already deployed application, for example dropping them into some specific directory, to enhance the functionality of the virtual machine, without them being necessary for its structure. For example, the virtual machine supports many different architecture, and the end user, having a virtual machine application installed on his system, could add a new architecture by dropping an appropriate plugin archive to the correct folder, after which the application will pick up the new architecture at startup. This is handy because we don't want to require building and releasing a new version of the application only to add a new architecture, or a new supported assembler or compiler.


### References

- https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
- https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html
- https://trunkbaseddevelopment.com/monorepos/
- http://www.plainionist.net/Implementing-Clean-Architecture-Scream/
- https://news.ycombinator.com/item?id=18808909
- https://medium.com/@mattklein123/monorepos-please-dont-e9a279be011b
- https://medium.com/@adamhjk/monorepo-please-do-3657e08a4b70


## Status

Proposed


## Consequences

The application clearly states its intent, listing features and use cases in `application/`, while the other modules are still clearly categorized by layer (and thus abstraction level). 

The build system must be able to support dependencies located in different directories, instead of everything being located in a single `lib/`, `vendor/` or such.
