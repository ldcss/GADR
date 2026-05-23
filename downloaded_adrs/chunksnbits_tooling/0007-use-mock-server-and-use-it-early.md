# Use mock server in your project setup and set it up when you start your project

* Date: 2019-03-02

## Context and Problem Statement

As most web applications rely on data from one or multiple API services, this creates a dependency that effects the development and testing for the application to be build.
Out of this situation a number of issues can arise:

* API development can often not be fully synchronized with frontend development
* Technical issues / development delays in the development of the API service impact frontend development as well
* Testing, esp. UI-tests rely on data on scenarios to be able to test core aspects of the application.
* Testing should be done on isolated datasets, which is not supported by all API services
* Issues / downtimes of API services impact development progress of web development team

## Considered Options

Create or use an existing mock server to allow development and (partially) testing without relying on the availability of (external) API services.

Existing solutions:
* [ng-apimock](https://www.npmjs.com/package/ng-apimock)

## Choosen Option

**Reasons**

**Notes**

## Background information
