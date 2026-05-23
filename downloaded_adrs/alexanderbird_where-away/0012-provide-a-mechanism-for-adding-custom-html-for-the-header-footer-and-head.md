# 12. provide a mechanism for adding custom html for the header, footer, and head

Date: 2020-11-15

## Status

Accepted

## Context

### Why custom HTML?
For deploying a where-away site, I have a few considerations:
 - For my personal links that I'll publish at a public domain, I'd like a service worker to cache the html
 - For the demo site, I'd like a header and footer to give context and to link
   to the Github repo
 - down the road, I can imagine making the CSS themable by having colors in CSS
   custom properties. I would like a way to conveniently override those colors
   when I use where-away.

By accepting optional HTML strings to include in the head tag, at the start of
the body tag, and at the end of the body tag, one can do all the above things
and more. It's cheap to implement and easy to explain.

### Alternative implementations

1. Update the bookmark xml format to accept those items
2. provide CLI arguments to pass in those strings
3. accepts paths as CLI arguments and read those files

### Considerations

I'd like this to be an opt-in feature -- it should be optional. Alternative #1
makes the xml input format more complicated for everyone, even if you're not
using this.

I'd like the implementation to be as cheap as possible for now, and #2 is
cheaper to build than #3 -- fewer edge cases.

Down the road, #3 seems easiest for the customer -- and on a related note, it
would be nice to be able to provide a path to the input file instead of piping
it in through stdin. I could imagine a where-away config file with paths to
these different html blocks, path to the input xml, etc.. Also, there could be
cli parameters if you don't want to author a config file. BUT that's too much
work for now. 

## Decision

Accept CLI parameters (optional) for document head, body header, and body footer
html.

## Consequences

It'll be a long, unwieldy invocation for the CLI. I'm pretty sure I'll get sick
of that and implement the more customer-friendly config file alternative down
the road. It's a two-way door, though -- I can follow later with the config
enhancement.
