# Using Regular PHP Session for storing Last Seen data

Date: 2020-09-07

## Status

accepted


## Context

We need this to make the 'Referrals Notification' work.

Needed a way to store the 'last_seen' value during the whole session. Because it is updated every hour by a middleware, we can't use it directly from the user model / database, as that would cause us to never show a notification ('last seen' is updated before we even get a chance to show it on the page.)


### Options

1. Laravel Sessions - Didn't work
2. Regular PHP Sessions

## Decision

Option 2 worked, so it's implemented.

In the LastSeen middleware we check for a 'prev_last_seen' session variable. 

- If missing, we update it with the 'last_seen' value. 
- If it exists, we don't change it.
  
Later, the User->hasNewReferrals() checks it to determine the right cutoff time, either 10 days ago or the more distant 'last_seen' value.

## Consequences

* We now always start the PHP Session, including in the tests, but it doesn't intefere with anything.
