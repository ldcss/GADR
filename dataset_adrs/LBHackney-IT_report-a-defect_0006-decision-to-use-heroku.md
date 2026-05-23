# 6. Decision to use Heroku

Date: 2019-05-09

## Status

Accepted

## Context

The team only have 10 weeks and 1 engineer to complete this work. 

Hackney already have at least 2 services (Report a Repair and Repairs Managament) on Heroku.

Hackney's playbook includes the decision to use AWS ECS as the container hosting platform of choice: https://github.com/LBHackney-IT/API-Playbook#hosting

Hackney are currently procuring their own Heroku account.

## Decision

Host the containerised service on dxw's Heroku account.
 
## Consequences

We will be spending more money by deferring the operations to Heroku instead of the team however this will enable us to save significant amounts of time getting set up and can instead focus more on meeting user needs within the application.
