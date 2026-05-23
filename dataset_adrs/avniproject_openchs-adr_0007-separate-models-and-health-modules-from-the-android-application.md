# 7. Separate models and health-modules from the android application

Date: 2018-05-16

## Status

Accepted

## Context

In the future, once all product features are built, there will be a lot of work on building and enhancing health modules. This might eventually also become its own project. 

There needs to be a contract that a health module exposes. We will have interfaces defined in the health module, and communication using the models (which will be common across openchs-android and openchs-health-modules). This will allow common domain logic to live in modules and health module specific business logic to live in the models. 

## Decision

The android client will be broken down into 3 components - openchs-android for the app, openchs-health-modules for the health modules and openchs-models for the contract objects that will be exchanged by openchs-android to openchs-health-modules. 

## Consequences

 - There is no place for implementation specific modifications to health modules yet. 
 - Unit testing openchs-health-modules can be done without loading the entire app

