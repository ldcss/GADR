# Simulator webserver to communicate with Nozama app.

## Status - accepted

## Context

Since we decided to design the simulator as a separated component we didn't thought how it would communicate with the WebApp. So, the simulator is a simple java program that can't do anything to communicate with Nozama since it is a web application and has a different ecosystem (spring framework).

## Decision

As of now we decided to create a simple webserver to expose simulator to our main WebApp. As it main functionality is to just pass some data when required and send notifications to Nozama's backend when some task is done.

## Consequences

- Now developers have a fully webserver for the simulator that can be highly configured and serves all the functionality we can provide(data polling...).
- Can be `dockerized` easily and set to be used as another service in a `docker-compose.yml` file for development environment.
