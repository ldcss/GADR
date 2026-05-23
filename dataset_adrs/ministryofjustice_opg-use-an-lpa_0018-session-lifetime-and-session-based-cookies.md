# 18. Session lifetime and session based cookies

Date: 2020-04-27

## Status

Accepted

## Context
 
We need to supply the user with prompts that they have been logged out due to inactivity. This is not currently possible
due to our session lifetime being dictated by the expiry of our session cookie (currently 20 minutes). Once a cookie has
expired we do not recognise a user in order to tell them that they have been logged out.

## Decision

* We will lengthen the cookie expiry to be as long as the business requires to display a _"logged out due to 
inactivity"_ message. Somewhere in the region of 1 day - 1 week will likely be acceptable.
* We will store the last access time of the user within the cookie and compare that upon new requests with our 
desired session time (20 minutes). This middleware could then force a user to re-login with an appropriate message if 
the time has expired.

## Consequences

This will increase the size of the session cookie but we believe it is still below the size where we would consider 
moving to different infrastructure (session information stored within AWS). We will revisit this issue when any further
additions are made.
