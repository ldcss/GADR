# Give creatures and the player character the same command/control infrastructure

## Active
  * Decided: 2018
  * Recorded: 2019-05-31


## Context

The 'core mechanic' of this game is the player being in control of allied plants.  There may be other cases of player control of other in-game entities as dev continues, but this is core.

Giving creatures and the player character pluggable command/control is more dev overhead.  As a spare time project, any choice for extra complexity deserves extra scrutiny.  On the same wave, though, the outcomes which can justify the extra effort are a larger set:  Not just important functionality, but significant learning and straight pleasure in craftsmanship can be enough reason.

This offers options for reuse.
If our guy is terrified, the player's InputCommandSource can be temporarily replaced with a FleeingCommandSource (or some such).  When the player is in charge of other entities, they get an InputCommandSource themselves, and will naturally be controlled by the player when their moments to act arrive in the schedule.


## Other Options

Develop the two as unrelated code, and approach the control of plants in a different way, later.  Of course, this includes knowing that the gap exists to be crossed, so remaining aware in the meantime of opportunities to cross it.

Investigate how other roguelikes have done this.

Give up on this aspect of the core mechanic, and have only autonomous allies.


## Decision

I'll do this.  It feels correct, and it trends toward the sort of wins and frustrations I'm hoping for in this project.  That is, where my decisions, rather than the guts of frameworks, are what I'm wrestling most often.


## Consequences

More complex code earlier.  A risk that combining the functions in this way will give me a problem that I solve poorly, with unpleasant/buggy code in the end.

A good chance of further beneficial fallout.

Actual interesting code to write.
