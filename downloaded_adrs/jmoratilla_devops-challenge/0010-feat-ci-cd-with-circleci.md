# 10. feat-ci-cd-with-circleci

# 8. feat-about-cicd

Date: 2020-02-20

## Status

Draft

## Context

Time to work on the CI/CD solution.

I need a job manager to build, test and deploy the apps to the kubernetes
 cluster.

I know there is a lot of documentation about jenkins, but I have been working
in the last years with other solutions like:

* SolanoCI (now closed)
* CircleCI

So I need to see if there is a way to use my knowledge in CircleCI or not.
  Besides, CircleCI has a free plan very useful for testing.

I know there is a jenkins-x product, but I don't have a clear idea about
 it.  I installed it and spent couple of hours to make it work (jx) but I got
 an error downloading kops, and I couldn't go further. 


## Decision

Try first with CircleCI to see if I can deploy the apps to kubernetes.

As I'm using a monorepo, all the apps are within the same repository, so we
 cannot separate the building process of each microservice.  All them will be
 build and deployed as one.

But if nothing has change in the app, then the building process will be faster.

Testing will be peformed on all apps secuentially, and some tests could be
 performed on all services without implementing mockups.

This way, when a event is received by the CI, a script will be executed to 
 execute the actions on each app.

 

## Consequences

