# 2. Not cloud agnostic

Date: 2017-11-22

## Status

Accepted

## Context

Since Cloud Security Watch specifically aims to monitor for 
misconfigurations in AWS accounts it does not make sense to 
make the tool cloud agnositic. 

## Decision

Whilst we support the notion of writing cloud agnostic 
code in general. In this instance it is not appropriate 
or desirable. 

## Consequences

Making the tool cloud agnostic would mean that the built-in
mechanisms like IAM roles and instance profiles would not 
be available to make cross account requests. 

By utilising AWS specific functionality we can make the 
tool considerably simpler. 
