# 3. Use Brunch

Date: 2017-06-30

## Status

Accepted

## Context

The styling of sites developed for NHSUK need to be as consistent as possible.
Currently each new site starts by copying what the last developed site had done
and building on that. This results in the newer sites looking different than
the older sites, which would not be a problem if each site was easily updated
to use the same, most recent, set of styles. Currently there is no central
store for the styles which means there is no easy way to find and use them
either.

The ability to review the styles in a development environment before they are
made available to a wider audience is important. As is the ability to use well
known technologies such as [SASS](http://sass-lang.com/).

## Decision

We will use [Brunch](http://brunch.io/) to accomplish a number of tasks
including:
* Running the site used in the development environment
* Generating the compiled assets

## Consequences

Using Brunch means there is some additional knowledge required about how it
works. However, this is offset by the ability to add a host of extra
functionality via [Plugins](http://brunch.io/plugins).
