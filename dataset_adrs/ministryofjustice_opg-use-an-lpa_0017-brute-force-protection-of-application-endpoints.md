# 17. Brute force protection of application endpoints

Date: 2020-04-22

## Status

Accepted

## Context

 > This ADR details the mitigation of brute force attacks on certain endpoints - other types of protection are out of 
 > scope.

We have a need to mitigate brute force attacks on certain endpoints in the application. Currently these are:

 * Actor Login
 * One Time Passcode (adding an LPA)
 * Viewer Code (viewing an LPA)
 
Brute force can be defined as multiple failed attempts to carry out these actions.

## Decision

Protecting against these kinds of attacks is a problem in two parts; reliable identification of users and the recording 
of attempts by that user against protected endpoints.

#### Identification

The bare minimum of information that we can use to identify a user is their originating IP address. This is not without
issue as it can be spoofed, or more likely the user is behind a NAT or proxy layer (as will likely be the case with our
corporate users). We can couple the browser sent headers that offer extra user identifying information (such as 'Accept'
'DNT', 'User-Agent' etc) in a hashing function to generate an ID that should more uniquely identify a user.

We will identify users using a hash calculated using the incoming IP and associated headers.

We will track this identity in the session to guard against changing headers within a session.

#### Attempt Tracking

We will use a cache service (AWS Elasticache) to track failure attempts at each of the three endpoints defined above.

We will use a per-endpoint moving window rate-limit to reduce brute force impact - these will be individually 
configurable in terms of window size and request limit.

## Consequences

This will introduce a new piece of technology to the stack - a Redis based Elasticache.

Identification of users is a tricky issue and prone to abuse. Further refinements on the approach will need to be
made.
