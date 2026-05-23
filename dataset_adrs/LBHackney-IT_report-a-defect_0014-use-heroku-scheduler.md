# 14. Use Heroku scheduler for recurring tasks

Date: 2019-11-27

## Status

Accepted

## Context

There is a user need to receive daily emails around a certain time.

Heroku Scheduler is a free service created by Heroku that lets you schedule
tasks to run at specific times.

Hackney have already used Heroku scheduler in the [Hackney Repairs project](https://dashboard.heroku.com/apps/hackney-repairs-production/scheduler).

## Decision

Since there is an established pattern of using Heroku Scheduler in other projects
we should continue this pattern by adopting it in this project.

## Consequences

Creating or editing a recurring task will require access to the project on
Heroku.

Heroku doesn't give guarantees that things will run precisely on time. A high
level of precision is not required to meet our user need.
