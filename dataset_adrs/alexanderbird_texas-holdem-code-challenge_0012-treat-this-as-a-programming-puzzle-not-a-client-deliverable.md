# 12. Treat this as a programming puzzle not a client deliverable

Date: 2019-06-03

## Status

Accepted

Extended by [13. Show no kickers for ties](0013-show-no-kickers-for-ties.md)

## Context

Based on the instructions, this is a "Programming Exercise" and the solution
should be "production level".

It is also in the format of a well specified programming puzzle: the
"Specifications" section is very precise.

If this were real-world software, I would not ignore invalid inputs and the
like. Even if it's not beautiful, some basic input validation would be expected
-- sooner or later someone's going to type in the wrong thing, and a messy stack
trace is not a nice user experience. (On the other hand, if it was a programming
competition, I would not think twice about believing the specification.)

I would also review things like performance requirements ("You described
inputting one game description at a time, is that right? Or will you need to
process batches quickly?").

Further, I would want to demo the application before delivering it to check that
I haven't made any silly assumptions.

However, this is neither a programming puzzle nor a client deliverable, it's a
job application. My guess is that Darryl isn't interested in rounds of iteration
to make sure I've built him just the right thing -- I'm guessing it's more about
seeing my process, the code I write, and the sorts of things I'm thinking about.

So, in the interest of time and understanding the essence of this task:

## Decision

I will treat this as a programming puzzle and not a client deliverable. I will
take the instructions at face value and forsake the client feedback sessions.

## Consequences

I will complete this exercise sooner and with less code.

If I guessed wrong and my reviewers were looking to see that I asked for
clarification and treated them like a client, I can at least refer to this
decision log to show I was thinking about it, even if I chose not to act on it.
