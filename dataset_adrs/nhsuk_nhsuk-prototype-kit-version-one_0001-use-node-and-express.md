# 1/ Use Node and Express
**Author(s)**: Steven Adams   
**Status**: Accepted   
**Date**: 29th August 2017

## Context
The prototype kit application will need to operate similarly to a live service, depending on the level of fidelity required for testing. This means that a server is required. To make the prototype kit easy to use for different levels of coding experience we want to implement auto routing (or route matching) for template files, the simplest way to achieve this this dynamically is to have an application running on a server.

## Decision
We will use Node.js with the Express framework to run a Node.js server for the prototype kit on both local development environments and production environment when published on Heroku. Node.js is written in javascript and is therefore one the most common languages between designers who have some coding experience and software engineers. It is also the easiest runtime to install on both Mac and PC.

## Consequences
There is a dependency on consumers of the prototype kit to have a compliant version of Node.js and NPM (Node Package Manager) installed on their machine.
