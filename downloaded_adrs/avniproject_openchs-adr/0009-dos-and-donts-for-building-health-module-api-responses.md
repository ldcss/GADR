# 9. Dos and donts for building health-module api responses

Date: 2018-05-16

## Status

Accepted

## Context

Some rules regarding usage of health-module apis. 

## Decision

Input for health-modules can be anything from openchs-models
Output of health-modules is loose right now. There is no reason at present to fix this. 
If a method returns an array of decisions, it has to return the same array everytime. For example, if it has [{"highRisk": ['overweight']}], even if there are no high risks detected, decisions have to return ['highRisk': []], and not an empty array. 

## Consequences
