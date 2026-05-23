# 7. Optimize for testability and readability rather than performance

Date: 2019-05-29

## Status

Accepted

## Context

Given a brute force algorithm for determining winners:
- There are 7 choose 5 hands possible per person (21), and one of those is
  playing the board (all five community cards) which is the same for every
  player. So, to enumerate all possible hands, we enumerate 1 + (20 * n) hands.
  O(n)
- For a given hand, an absolute score can be calculated in linear time:
  1. match the hand against the pattern of each of the 10 possible hands until a
     match is found. O(1)
  2. If that hand doesn't use all five cards, make note of the kicker values.
     O(1)
- For each player, sort hands by absolute score and choose the highest. There
  can only be 21 hands, so O(1)
- For all players, sort by score of highest scoring hand. I don't know what
  algorithm Node uses for sorting, but that would determine the complexity of
  this step.

Each of those steps is O(n) or O(1), except for the last one which is a
single sort operation.

The overall complexity is somewhere around O(n log(n)) or O(n^2), where n is the
number of players... which will probably be less than 10. 

All this to say, performance is not likely to be a big consideration.

In the absence of other factors, testability and readability are good
architectural values -- they make it so we can respond to change and
collaborate -- so if we need to optimize for something else later, it's easy to
do that.

## Decision

Optimize for testability and readability.

## Consequences

- I can implement whatever object-oriented design is easiest to think about and
  test
- Given the choice between performance optimization and readability, I choose
  readability
- If I discover a performance issue, then I'll revisit this decision
