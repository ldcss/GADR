# 4/ Use NPM scripts and Gulp for running tasks
**Author(s)**: Steven Adams   
**Status**: Accepted   
**Date**: 29th August 2017

## Context
There are lots of different tasks that need processed in order to get the prototype kit up and running. Tasks such as; installing dependencies, moving files from dependencies into the app file structure, and most importantly - running the application.

## Decision
We will use a mixture on NPM scripts and [Gulp](https://gulpjs.com) to run our tasks. NPM scripts give us the core installation and start tasks as well as the ability to run Gulp tasks. Gulp, written in javascript, is very extensible and will allow us to have complete control over compilation and assembly of the applications assets.


## Consequences
There will need to be instructions written and made available to tell consumers of the prototype kit how to set a username and password. There will have to be settings put in place to enforce the use of a username and password when a prototype is published.
