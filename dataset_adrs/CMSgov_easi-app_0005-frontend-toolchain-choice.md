# Use Create React App for frontend bootstrapping

* Status: Proposed [Proposed, Accepted, Rejected, Deprecated, Superseded, etc.]
* Deciders: Mikena, Eady, Chris
* Date: 2019-10-17

Which React toolchain should we use to bootstrap CMS EASi?

Bootstrapping a project is usually a tedious and time consuming task. It
involves setting up a module bundler, configuring a JavaScript compiler as
well as wrangling all the dependencies to begin application development.
Setting up an application from scratch or using an existing toolchain both
have their pros and cons and these are points we want to explore.

## Considered Alternatives

* [Create React App](https://github.com/facebook/create-react-app) (CRA)
* Create React App w/Truss USWDS
* Truss' Create React App fork
* Roll up a new application from scratch

## Decision Outcome

Create React App (CRA)

* `+` This is a React toolchain we have experience using
* `+` Do not need to spend time tinkering with configuration
* `+` Provides an [eject](https://create-react-app.dev/docs/available-scripts#npm-run-eject)
command to gain full control of the build tool and configuration choices
* `+` Very well known toolchain that has a lot of tools to support it
(e.g. [craco](https://github.com/gsoft-inc/craco) and [rescripts](https://github.com/harrysolovay/rescripts)
* `-` Do no have full control over configuration files in case we need
customization
* `-` Ejecting is a one-way operation. Once you eject, you can't go back!

## Pros and Cons of the Alternatives

Create React App w/Truss React USWDS Library

* `+` Can leverage component library that Truss uses on other projects
before it goes open source
* `-` The library is still in its early stages; not mature yet
* `-` Because of its infancy, library and/or EASi can be a roadblock
Note: This Truss React USWDS Library is a NPM package that we can
import in the future. The decision here is that we will build out React
components on our own rather than leverage an NPM package.

Truss' Create React App fork

* `+` Truss toolchain with tools/libraries that we are comfortable using
* `-` Somethings are still being worked out and not quite ready

Roll up a new application from scratch

* `+` Complete control over configuration
* `-` Lots of initial work and maintenance over time
* `-` Lots of additional decisions to make on build tools and versions
