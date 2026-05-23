# Apps and Page Models

## Summary

### Issue

We need to define a strategy for our page model definitions to ensure that our code fits the project requirements.

### Decision

* Remove the `content_platform` app.
* Migrate all main page models into one app.
* No longer use the concept of "products".

### Status

Accepted

## Detail

### History

In the past, we defined our apps based on the assumption that different areas of the website were managed by different teams with different requirements - called "products".

* Behind The Headlines
* Conditions
* Guides
* Medicines
* etc.

Since this project was started, there have been changes to make the different content areas look and behave more similar to each other. This means that our apps which used to be different, now share a lot of similar code.

At the very beginning of this project, there was a concept of a "core" CMS app called `content_platform` which contaied shared components with other projects. Those other projects have been phased out, so there is no longer a requirement for the `content_platform` app to be separate.

An Information Architecture team has been created which is defining the structure and enforcing consistency in our page models.

### Current state

Currently we have:

* A `content_platform` app.
* A suite of apps in the `products` module.
* A suite of apps in the `core` module.

### Target state

* A suite of apps in a `core` module providing site-wide functionality that make sense as standalone apps, where a standalone app is the smallest unit that other people might realistically want to use in a different project.
* One app containing NHS.UK Wagtail models and related code.
* One app containing Campaigns Wagtail models and related code.
