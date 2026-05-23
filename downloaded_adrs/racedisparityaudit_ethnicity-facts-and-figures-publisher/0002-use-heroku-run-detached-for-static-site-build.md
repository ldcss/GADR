# 2. Use heroku run:detached for static site build

Date: 2018-12-05

## Status

Accepted

## Context

At the moment, we have a set of scheduled tasks on Heroku that run every 10 minutes, hour, or day. These range from building the static site (every 10 minutes), to reporting stalled builds (every hour), to refreshing the database from production data (in dev/staging, every night). The main job here, building the static site, has started to fail because it occasionally runs longer than 10 minutes. The Heroku scheduler will only allow a scheduled instance to live for as long as the interval on the task. Heroku is therefore killing the instance before it can finish, leading to the incomplete builds and frequent reports of 'stalled' (in this instance, killed) builds.

We need to schedule static site builds in a way that removes this strict time constraint so that they will always finish building.

## Decision

We will continue to use the Heroku scheduler on a ten-minute interval, but will instead use the Heroku CLI to run the management command (./manage.py build_static_site) in a separate, detached worker dyno. This worker dyno has a lifespan of 24 hours and is not limited to the interval of the scheduled job.

The command we will use is `heroku run:detached -a <app_name> ./manage.py build_static_site`.

Pros
----
* Very easy to implement.
* Will allow static site builds that take up to 24 hours (which is greater than any reasonable build length).

Cons
----
* We remain unable to responsively schedule static site builds at the moment they are needed and rely on the scheduler to kick off a build.
* We have to expose a Heroku API key and install the Heroku CLI buildpack on our main Publisher app.

## Alternatives

We could create a separate repository/app pipeline with an attached scheduler that runs management commands. This would let us isolate the Heroku CLI buildpack and API token away from the main webserver, but would mean managing another pipeline and slightly decrease visibility of what's going on, as it's unlikely we'd be looking at that pipeline very often. It also does not feel like there is a significant need to isolate the buildpack or API key - if someone can access our app's environment or servers, we're already too compromised.

Another option is to spin up detached apps directly from the web server. We could remove the scheduler entirely and use a Python Heroku lib to run the relevant management commands at the time they're needed (e.g. after a user published a new page). This would make the app less responsive and builds more fragile, as there wouldn't be anything to check whether any builds have been requested on a regular basis. It also would tie the app in more closely to Heroku and cause peculiarities when running on dev machines.

A third implementation would be to build out a queueing system and have the scheduler submit jobs for workers to process. This would likely involve additional infrastructure (e.g. redis) to support the job queue, as well as require writing worker code. We would need additional monitoring, maintainenance, and testing. At the moment, it is more work than this problem requires to solve satisfactorily. Many more mature infrastructures will have some manner of queueing system or async processing system to offload long-running or IO-based workloads, but at this time it feels like we can still function without that functionality given a limited and mostly-internal userbase that is more tolerant to processes happening at scheduled intervals rather than near-real time.

## Consequences

We have three tokens linked to the RDU Developers Heroku account (one each for dev/staging/production). These tokens have no expiry date. Builds will continue to be checked only on a 10-minute schedule.

All of our Publisher Heroku apps now contain the Heroku CLI buildpack, which is not actually used by the web server, but just by the scheduler (which runs on the same app slug).
