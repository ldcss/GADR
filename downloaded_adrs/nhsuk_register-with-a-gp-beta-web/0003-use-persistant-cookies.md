# 3. Persisted or Session Cookies

Date: 16/03/2017

## Status

Accepted

## Context

### What is a cookie?

A cookie is a small amount of data sent along with every HTTP request to a
website. We can set it to any value we like. In this project we are using the
cookie as a way to store data that a person who is registering has given us.

Cookies constitute a security risk as they can be intercepted in flight or
on machine of the user. That's why we want them hanging around for as little
time as possible.

### What is a Session Cookie?

A session cookie is a cookie that disappears when a browser window is closed.

### What is a Persistent cookie?

A persistent cookie is one that disappears after a set time, called its
`max-age`. 


### Assumptions

  * More people are using their own devices than public ones
  * We will set a sensible (short) `max-age` on a persistent cookie
  * People rarely close their browsers

## Decision

### Use session cookies

Given that most people will be using their own devices, and most likely their
phones it makes more sense to use persistent cookies with a short timeout rather
than a session cookie which could lie around on their device for months.

## Consequences

One of the consequences of using persistent cookies is that:

 * if someone abandoned the registration journey
 * on a shared or public device 
 * someone uses the same device after them (but within our `max-age`)
 * the second person also goes to our services
 
then the second person will be able to see whatever information the first person
entered.
 
The consequence of using a session cookie is the same as above if the first
person didn't close their browser before the second person took over, but in
addition to that even on a personal device, their personal information will be
available for an unknown amount of time because we don't know when, if ever
they'll close their web browser (all tabs).
