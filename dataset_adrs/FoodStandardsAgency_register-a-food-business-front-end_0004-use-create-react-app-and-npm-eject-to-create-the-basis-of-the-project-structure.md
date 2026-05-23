# 4. Use create-react-app and npm eject to create the basis of the project structure

Date: 2018-05-15

## Status

Accepted

## Context

React projects can be created from scratch, by setting up webpack scripts, installing dependencies etc. or they can be set up to a predetermined configuration using the create-react-app CLI.

## Decision

We will use create-react-app to generate a project scaffold using Facebook-defined best practices.

We will use the `npm run eject` command to make full project configuration available to us, such as Webpack.

## Consequences

We rely on the Facebook team to provide high-quality code as a basis for our project.

We get up and running very quickly with a scaffold that uses coding best practices and can begin writing React code without learning Webpack etc. in depth.

We can configure the project to our bespoke requirements as and when changes become necessary.

We must manually apply package and standards updates to our project when they come in the future, rather than receive them through a simple create-react-app update.
