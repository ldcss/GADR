# Supercedes is not transitive

*Number:* ADR-0004

*Created:* 2019-04-02 06:34:36 +0000 UTC

*Status:* Accepted

*Authors:*
- James Rivett-Carnac
- Zulfa Achsani


# Background

Lets say I decided to store all ADRs as XML in ADR-0001
and then I stopped being drunk; so I now need to make a new
decision.  I write a new ADR, which is ADR-0003, which says:
store all ADRs as json and supercede ADR-0001.

ADR-0001 is updated and says superceded by ADR-0003.
Later I realize i'm a fool, and JSON doesn't support really anything
coherent.  So i say: ADR-0005 supercedes ADR-0003: use YAML or TOML

# Complication

Do I also updated ADR-0001, and say its superceded by ADR-0003 AND 
ADR-0005

# Options Considered

1. Yes: semi-clearer chain of decisions, go and update the entire chain of ADRs on new
ADR creation
2. No: easier to program, can recover the chain of decisions using a DAG later
you just update the specified ADRs only, and not their 'parent' ADRs.

# Decision

2) actually preserves the timeline better without extra effort. So do 2.

# Outcome

Needs implementation

