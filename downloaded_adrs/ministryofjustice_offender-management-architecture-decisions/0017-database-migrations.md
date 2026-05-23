# 17. Use blue-green deployments to manage database migrations

Date: 2019-01-24

## Status

Accepted

## Context

We have reached a point where we are going to start reading and writing data to our Allocation API application database and will need to manage database migrations when adding tables, columns and so forth.  This ADR decision outlines the agreed upon approach that the team will take for managing these migrations.

## Decision

We will use blue-green deployments split into the following steps (using adding column as an example):

* Add a database migration that inserts the new column
* Update the application so that all new data gets written to new column
* Run a task to copy all the data from the old column to the new column
* Update the application so that it reads from the new column
* Add a database migration that removes the old column

We will also ensure that any migrations include 'up' and 'down' methods, rather than just 'change' to avoid any situations where Rails doesn't know how to handle the inverse of the up or down.

## Consequences

This will reduce downtime, and reduce the risk of losing data as we can more granularly control individual tasks rather than it happening in one big bang type event that you can't recover from.

Another ADR will be required once we have researched, discussed and decided on how we will manage situations involving rollbacks.
