# 11. Sort hands with a single hexadecimal string

Date: 2019-06-01

## Status

Accepted

## Context

Hand rank is a function of:
 - rank of the hand type
 - value of the cards relevant to the hand type
 - value of the kicker cards

I could implement the sort by putting all those values in an array and comparing
item by item.

A string comparison would be awkward because some values need two digits.

I could zero pad them, but an easier approach would be to base-16 encode them.

There are only 10 hand type ranks, and only 13 card values, so each value will
only need one hexit.

By producing an alphabetically sortable string for each hand, a simple less-than
operator will do the trick.

## Decision

Sort the hands with an alphabetic comparison of a hexadecimal string encoding
all values relevant for relative hand rank.

## Consequences

The solution is a little more "magic", which can be more confusing. But, it's
simpler than the imperative number array comparison approach, which makes it
easier to implement.
