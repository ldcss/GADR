# 6. Feature Toggle Defaults

Date: 2019-05-21

## Status

Accepted

## Context

This module utilises Feature Toggles. It has toggles to determine:

* If any resources should be created
* If a DynamoDB table resource should be created
* If an Autoscaler should be enabled

These features need some default values.

## Decision

All of the Feature Toggles are defaulted to on ("true") at this time.

We believe that in most cases people will want to create a DynamoDB table with
Autoscaling at this time.

## Consequences

Out of the box DynamoDB table resources will be created with Autoscaling
enabled.

To turn off the feature toggles you will need to set the appropriate flag to
off ("false") using the apporpriate mechanism based on consumption method.
