# 9. use-sidekiq-and-redis-for-asynchronous-tasks

Date: 2019-06-24

## Status

Accepted

## Context

- This service is sending multiple notifications by email and SMS to various users and is a core part of the value it provides
- There are no services or strategies described in the API documentation as of today https://github.com/LBHackney-IT/API-Playbook.
- Another Hackney Rails service is using a Shopify gem called DelayedJob with ActiveRecord https://github.com/LBHackney-IT/repairs-management/blob/develop/Gemfile#L56
- I haven't used DelayedJob before
- I have used Sidekiq and Redis quite a lot
- Choosing Redis and not using Postgres for the data store will offer more advantages in the long run, such as using it for feature flagging and short term counters. Decoupling from Postgres also allows ensures that we don't go over our Heroku database usage by accident
- There is only 4 weeks left of this project and we've only carved out a small time to make these synchronous tasks asynchronous so time is a big factor at the moment
- Sidekiq and Redis are well known services and tools in the Rails community

## Decision

Use Sidekiq and Redis for Asynchronous tasks

## Consequences

- A new Heroku addon will need to be configured
- We won't be aligned with at least one other Hackney project
- Future develpoment may have more options open with this choice of design
- Separating queue backends offers a long term advantage after a short term cost
- I will be able to set up Sidekiq and Redis quickly without learning an alternative tool. We will therefore hopefully be able to deliver more of our roadmap by the time the project ends

