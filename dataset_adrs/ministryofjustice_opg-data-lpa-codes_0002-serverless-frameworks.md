# 2. Serverless Frameworks

Date: 2020-04-29

## Status

In progress

## Context

We currently use Terraform to manage infrastructure across OPG projects. This is great for AWS services but
makes local development of certain AWS services (eg Lambda functions, API Gateway) difficult.

There are a lot of frameworks around that claim to make developing & deploying serverless apps easier. Our real interest
is making local dev simpler, as we already have a nice pipeline working with Terraform & CircleCI for the infrastructure.

Here is a (not exhaustive) list of options:
* The big one: [Serverless](https://www.serverless.com/)
* Python specific: [Zappa](https://github.com/Miserlou/Zappa)
* Made by AWS: [Chalice](https://chalice.readthedocs.io/en/latest/)
* More AWS: [SAM](https://github.com/awslabs/serverless-application-model)
* Not a framework: [LocalStack]()

#### Serverless

The only instructions I can find for local dev are basically how to test a function by mocking out AWS things, there's
nothing specific to Serverless. It is mainly deployment focussed, and all that is done through Cloud Formation and 'magic'.

It also appears that the Pro service is [not free](https://www.serverless.com/pricing/)

[Serverless Local Development](https://www.serverless.com/blog/serverless-local-development/)

[AWS HTTP APIs](https://www.serverless.com/aws-http-apis/)


#### Zappa

You can start up a full local version of your stack using Zappa, but that requires you to set up all the deployment
through the framework too, which we would rather not do.


>Zappa has one thing I personally don't like. I want my cloud deployments to be managed through an orchestration service, as this gives you a single place from where all the resources that belong to a deployment originate. For AWS, you can use the native Cloudformation service for this. Unfortunately Zappa uses Cloudformation only for a portion of its deployment tasks, and for the rest, it invokes AWS APIs directly. This makes keeping track of resources associated with a Zappa deployment harder.

-- Miguel Grinberg - [Serverless Deployments of Python APIs](https://blog.miguelgrinberg.com/post/serverless-deployments-of-python-apis#comments)

If Miguel "Ultimate Master of Flask" Grinberg doesn't like it, then we don't like it.

#### Chalice

>After a couple of hours, it’s pretty clear that Chalice is a clone of Zappa that adds some automatic IAM magic but offers a tiny subset of its functionality and requires significant code changes to my app.

-- A Cloud Guru - [The fear and frustration of migrating a simple web app to serverless](https://read.acloud.guru/adventures-in-migrating-to-serverless-a63556b39042)

It is actually a python app framework similar to Flask or DJango (tho way smaller), so if we were intending to use this
we'd have to write our code using Chalice from the start (or refactor).

I had a little play with this at the start of the Documents integration and had a lot of problems, though I can no longer
remember the details, I do remember having a lot of difficulty triggering the lambda locally, I think you have to use it
in combination with SAM CLI below.

#### SAM CLI

If you don't use it for deployments this can pretty much be ignored as a 'framework'. It can be used to invoke lambdas
locally however, see [Invoking Functions Locally](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html)
but it also cannot recreate API-Gateway functionality.

#### LocalStack

Not made a final decision on this, as it does a LOT more than just invoke a lambda function. The big downside here
is that [it is not free](https://localstack.cloud/#pricing). Might be worth returning to when we get deeper into DynamoDB
as it can mock out an entire AWS stack locally.

## Decision

We will not use a serverless framework, we will use Flask and Flask-Lambda to run and test locally.

This will be reviewed again once we start properly working with DynamoDB

## Consequences


