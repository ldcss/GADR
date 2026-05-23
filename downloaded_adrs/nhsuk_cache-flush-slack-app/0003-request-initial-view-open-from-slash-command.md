# 3. Request initial view open from slash command

Date: 2019-11-13

## Status

Accepted

## Context

When the app is running locally and being worked on during the development
process the speed of response from the functions is good enough so that the
request to open the initial view can be done once the request has been
validated. However, when deployed there appears to be an increase in the
response times. This isn't a problem for the majority of the interactions,
however, the opening of the initial view needs to be completed within 
[3 seconds](https://api.slack.com/surfaces/modals/using#opening_modals).
During testing there were many times the view wasn't being opened. The way to
mitigate this is to make the request to open the initial view asap within the
slash command life cycle.

## Decision

The request to open the initial view has been changed so it is the first thing
within the slash command life cycle.

## Consequences

The consequences include:
* the slash command isn't verified until after the initial view is opened
* an additional 'waiting for verification' view is required to be displayed
  whilst the verification happens in the background
