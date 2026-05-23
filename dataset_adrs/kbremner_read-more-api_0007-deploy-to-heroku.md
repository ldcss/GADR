# 7. Deploy to Heroku

Date: 2017-09-24

## Status

Accepted

## Context

The application needs to be deployed somewhere.

There are many container orchestration platforms for configuring a cluster of machines running Docker containers and managing the deployment of images on to these containers. Setting up these tools involves managing the cluster of machines and the hosting costs associated with these machines.

Heroku is a Platform as a Service (PaaS) provider which helps with the deployment of applications. They have a [Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime) solution that handles the deployment of Docker images in to suitable containers.

Heroku has several pricing tiers for machines that the application will run on, including a free tier.

Heroku provides a free hosted PostgreSQL option. It will handle setting a "DATABASE_URL" environment variable, containing the information required to connect to this database. The free tier database is limited to 10,000 rows.

We want the setup process to be as simple as possible.

## Decision

We will host the application on Heroku, using their Container Registry solution with a hosted PostgreSQL database.

## Consequences

We will have no costs associated with hosting the application.

The suitability of the free tier will need to be investigated if performance becomes an issue.

A database will not need to be setup seperately.

The suitability of the free database tier will need to be investigate if performance or the quantity of data becomes an issue.