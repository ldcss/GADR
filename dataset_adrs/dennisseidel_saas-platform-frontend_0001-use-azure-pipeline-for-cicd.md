# 1. Use Azure Pipeline for CICD

Date: 2019-02-23

## Status

Accepted

## Context

To automated your development you need a CICD platform that automated the build, test and deploy steps.

## Decision

I use Azure Pipeline to build, test and deploy.

## Consequences

it will allow me to integrate with github, build based on folders and therefore support mono repos without deploying everything for every change, integrate with a complete issue tracking tool, is free for public projects. It does not have a local builder like Google Cloud Build, I will have to see if this is a problem for debugging. It does not integrated as well into github as github actions, i will have to check them out when they are out of beta because cloud actions have a lot of pre developed libraries to integrate with Gitub, AWS, GCP, npm and more. 
