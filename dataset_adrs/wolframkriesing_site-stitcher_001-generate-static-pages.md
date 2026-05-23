# 1. Generate Static Pages

## Status

Accepted

## Context

I see so many thing broken on the web today, it is not only website speed, it is also
how many tools we have accepted to use to solve a simple problem. Especially in the JS
world I feel the healthy "How much do I need?" question is asked rarely. We also teach
newcomers that it is ok to load 1GB of npm modules before we can actually build an empty page.

In this repo I try to do the simplest thing possible to generate my website.
I am looking for dependencies that are as tiny as possible, some I just need to not use and
write the needed code itself, this also makes me aware how much of a dependency I would have needed
only.

Also the site that I want to ship shall have all a11y, lighthouse, etc. scores as high as possible
therefore the site shall degrade gracefully be accessible and very light weight.

I also want the simplest hosting setup and infrastructure possible, due to using github it might 
be github-pages, which is just static pages.

## Decision

With static pages the above can be achieved. Easily.

## Consequences

+ I might write more code myself, but I learn and practice
- it might take more time