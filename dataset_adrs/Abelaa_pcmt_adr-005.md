# 5. Build PCMT from the Akeneo PIM Community Edition

## Status

Accepted, 2019-07-01

## Context

The PCMT group is interested in starting from an existing code-base to decrease
our time-to-market and make use of our short available project time-line.  To do 
this the group created a simple [evaluation process][eval-process] by which we
[evaluated 14 mature software products][eval-matrix].  Out of this process a 
[recommendation][recommendation] narrowed the options down to 2, highlighting a 
few business-focused trade-offs between them. These trade-offs were captured in 
detail as a [pre-read to project stakeholders][pre-read], with the overall 
consensus being that neither option would be a wrong-option. 

[eval-process]: https://drive.google.com/open?id=1vG-kVU5Jfh28g63mI21Lp3OwH4Vmq562101g8VdAoLQ
[eval-matrix]: https://drive.google.com/open?id=19MLRJvzgIio41XjeefCc6z3ygrjiuVJLC11IxOHppoE
[recommendation]: https://docs.google.com/document/d/1GCAWtYuwSrUBp5zmaP5rCqVXPBdH_Rats4ib7ZZIuoo/edit?usp=sharing
[pre-read]: https://drive.google.com/open?id=17CWD5MBOTSuG1HtLHo0JQ_Y6E3L73IuVdIMzdfsJg48

## Decision

We will build PCMT from [Akeneo PIM Community Edition][akeneo-ce].

We will sign the Akeneo SAS [Contributor's Agreement][contrib-agreement] should 
we need to patch or otherwise contribute to Akeneo PIM Community Edition.

We will maintain an active down-stream fork of the Akeneo PIM Community Edition
git [repository][repo].

We will make every effort to be forward compatible with future Akeneo PIM
Community Edition releases.

[akeneo-ce]: https://www.akeneo.com/community-edition/
[contrib-agreement]: https://www.akeneo.com/contributor-license-agreement/
[repo]: https://github.com/akeneo/pim-community-dev

## Consequences

PCMT will leverage the Akeneo PIM Community Edition's modular architecture, 
including the use of the PHP Symphony framework.

PCMT will regard the Akeneo PIM Community Edition git repository as the
authoritative upstream repository, following that project's conventions and
release-cycle.

---
Copyright (c) 2019, VillageReach.  Licensed CC BY-SA 4.0:  https://creativecommons.org/licenses/by-sa/4.0/
