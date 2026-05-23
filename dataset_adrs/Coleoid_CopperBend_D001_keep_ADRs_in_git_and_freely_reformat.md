# Keep ADRs in git and freely reformat them

## Active
  * Decided: 2019-05-25


## Context

I feel that ADRs in some form may be very beneficial at Envisage, but two things make me reluctant to push the practice right now.  First, ignorance--I've never done this, so I can't talk personally about the experience.  Second, the enthusiasm of first encounter.  Both of these are addressed by actually doing it for a while.

Copper Bend is a learning/entertainment project.  Trying new techniques and technologies is a primary goal.

The Envisage products are very different from this one.  What works well here won't necessarily cross over.


## Decision

I will avoid tooling, and simply handcraft the documents.  I'll keep them in the main project repo.  I'll review periodically, trimming the present-but-useless and adding the missing-yet-promising.
I won't worry about synchronizing the format between ADR docs.


## Consequences

Due to the learning/fluid format intention, more time will be spent noodling with the structure of these ADRs, than with other options.


## Other Options

Create no documents, spend all my time hacking code.

Use an automated ADR framework software.

Use one of the existing formats.

Discuss ADRs immediately at Envisage.


## References

https://github.com/joelparkerhenderson/architecture_decision_record
  * Includes many formats and links outward

ADR Tools: https://github.com/npryce/adr-tools
  * Command line tools for managing ADRs
  * Includes its own set of ADRs.

Holochain Rust: https://github.com/holochain/holochain-rust/tree/master/doc/architecture/decisions
  * Highly technical in many locations

Eclipse Winery: https://github.com/eclipse/winery/tree/master/docs/adr

https://www.infoq.com/articles/sustainable-architectural-design-decisions/

https://www.youtube.com/watch?time_continue=2&v=41NVge3_cYo
    ADRs in use with IBM Watson
    
