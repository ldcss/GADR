## Tracking External Files (Revisited) <sub>ADR-003</sub>

### Status

_Accepted_

_Supersedes [ADR-001](https://github.com/slackwing/feathers/blob/master/adr/001-tracking-external-files.md)_

### Context

The strategy accepted in [ADR-001](https://github.com/slackwing/feathers/blob/master/adr/001-tracking-external-files.md) is difficult to recall, therefore difficult to be confide in. An alternative is proposed.

### Approaches

#### 1. Document logical changes

The main kind of external files we want to track are configuration files, such as .zshrc and .vimrc. For these, it would be better to document logical changes, _e.g._ as steps in [tooling](https://github.com/slackwing/feathers/tree/master/tooling), for at least 3 advantages: (1) logical changes are easier to comprehend than a raw configuration; (2) steps are pickable; and (3) layering configurations in steps is more robust, especially across different systems, than dropping them all in at once.

#### 2. Track snapshots

However, documenting logical changes comes with the overhead of having to prepare and finalize configurations for commiting. This in turn carries the risk of piling up uncommitted configurations. We can balance things by committing snapshots of raw configurations, _e.g._ in [tooling/snapshots](https://github.com/slackwing/feathers/tree/master/tooling/snapshots).

#### 3. Other external files

Currently there are no other kinds of external files we want to track. Disregarding.

### Decision

Adopting #1 and #2.

### Accepted Tradeoffs

None known.

### Retrospective

_TBD_
