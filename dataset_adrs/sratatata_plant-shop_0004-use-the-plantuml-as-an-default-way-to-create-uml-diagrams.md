# 4. Use the plantuml as an default way to create uml diagrams

Date: 2018-06-09

## Status

Accepted

## Context

It's occuring very often that drawn documentations is no longer up to date.  

## Decision

We are going to use [PlantUml](http://plantuml.com/) to store our diagrams in repository.

## Consequences

Everyone needs to write it's uml diagrams in clean plant-uml and still remember to update it in commit.  
Any code review shouldn't pass if plant-uml diagram isn't updated.
