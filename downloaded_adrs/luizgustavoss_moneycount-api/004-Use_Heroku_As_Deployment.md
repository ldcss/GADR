# Title: 004 - Use Heroku as Deployment Environment


## Status 

accepted


## Context 

It's desirable to keep the project online for testing purposes, and it has to be an easy to use environment with no cost.


## Decision 

I decided to use Heroku, as it has an easy to use environment, CLI tool that makes it easy to deploy with just few commands and has a free plan. It also has a great integration with lots of platforms and recognizes Spring Boot out of the box.


## Consequences 

A fast deployment process, smooth integration with Spring Boot and no costs. After 30 minutes of idleness the instance is turned off, but starts again, with a little lazy, after the firts access.
