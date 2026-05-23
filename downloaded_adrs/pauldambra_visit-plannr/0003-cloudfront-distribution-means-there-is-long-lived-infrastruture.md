# 3. cloudfront distribution means there is long lived infrastruture

Date: 2018-03-29

## Status

Proposed

Superceded by [6. collapse to one cloudformation template](0006-collapse-to-one-cloudformation-template.md)

## Context

The original intention was to be able to build the entire application stack from a single template. However, adding a [cloudfront distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) takes 15-25 minutes to complete.

## Decision

To have two infrastructure templates. One with slow to provision infrastructure. A second with the fast to provision infrastructure.

## Consequences

 1. Development sessions should begin by creating the stack described by the `static-infra-template.yml` file.
 2. Some resources will likely need known names so they can be referenced between the templates.
