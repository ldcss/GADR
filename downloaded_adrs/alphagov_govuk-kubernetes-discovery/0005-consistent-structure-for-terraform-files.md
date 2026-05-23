# 5. Consistent Structure for Terraform Files

Date: 2017-06-06

## Status

Proposed

## Context

We should have a consistent structure for working with our Terraform files. We
should be able to look into a file and understand it's function is and what it
creates, what variables it needs to run and what it outputs after it's finished.

We should not have to spend time picking apart the code to understand what is
created by Terraform.

We should not have to work with multiple files to understand a single component.

## Decision

Create style guidelines based upon the following:

 - Header with title and description
 - Variables listed
 - Outputs listed
 - Full descriptions of what variables and outputs do in the code
 - `terraform fmt` across each file

Create a style guideline document explaining this structure.

## Consequences

Code will have to reviewed by peers and asked to change formatting depending on the
styleguide.

Tests should include some level of linting using `terraform fmt`
