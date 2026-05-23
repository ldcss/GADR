# 5. Add Synthetic max-age to Session Cookie

Date: 26/04/2017

## Status

Proposal

Supercedes [4. Cookie Encryption](0004-cookies-encryption.md)

## Context

in [ADR#4](0004-cookies-encryption.md) we decided to use session cookies but
didn't address the problem of sessions lasting an infinitely long time if the
user doesn't ever close their browser (all tabs).

A user could abandon their registration and then return months or years later to register again and we'd have their information pre-populated. This will be extremely disconcerting for the user.


## Decision

Using middleware, add an extra key to the session cookie called max-age. If the middleware sees a cookie with a max-age < now then it will delete that cookie. We can set to a long time like 4 hours for now and reduce as we continue to learn about our users' behaviour.

## Consequences

* We add more complexity to the code-base
* Some people filling out their application over a period of days will not be
  able to complete their journey
* We have increased security for our users because the cookie containing their
  data doesn't stick around for an unbounded amount of time
