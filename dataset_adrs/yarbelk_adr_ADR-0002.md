# Use TOML for adr format

*Number:* ADR-0002

*Created:* 2019-03-07 05:58:30 +0000 UTC

*Status:* Accepted

*Authors:*
- James Rivett-Carnac


# Background

ADRs should be easy to work with with tooling, but also by hand if you're
somewhere far away from your normal setup.  It seems most people just use
markdown.  Coming from a python background, I am not against this, but
having used sphinx, I'm happy to separate the easy to read from the
easy to manage.

# Complication

Its not fun to muck about with markdown programatically

# Options Considered

1. Bite the bullet, do lots of parsing and regex
2. use a human readable format, convert it to markdown automatically

# Decision

1) Use TOML

I decided to try using TOML, because its super easy to edit
as a human.  The data structure for an ADR is simple enough
that It is *really* easy to work with programatically.

One thing to track is that the text block should use multiline format
to make it easier to read


2) Automatically render to GFM
There is a github flavoured markedown library for go, I will automatically
render out to it

# Outcome

