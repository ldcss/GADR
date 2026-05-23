# 13. Show no kickers for ties

Date: 2019-06-03

## Status

Accepted

Extends [12. Treat this as a programming puzzle not a client deliverable](0012-treat-this-as-a-programming-puzzle-not-a-client-deliverable.md)

## Context

I have chosen not to ask for clarification about the specification like I would
with a client -- instead, I'll make a sane decision and document it. The
specification is not totally clear on when kickers should be shown. It says "The
hand name should have a full description including kickers if necessary". When a
kicker resolves a tie, it should be shown -- it's necessary. But when the final
rank is a tie despite all kickers, should they be shown?

Yes: because they were considered when determining the rank.

No: because they were found to not impact the final rank.

Based on decision 0012, I'm free to make either choice based purely on
preference.

## Decision

"No", don't show the kickers for ties.

## Consequences

Same as 0012.
