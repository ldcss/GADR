# Use Markdown Architectural Decision Records

- Status: Pending
- Date: 2019-09-11
- Deciders: TBD

## Context and Problem Statement

We want to record architectural decisions made in this project.

Which format and structure should these records follow?

## Decision Drivers

- **Readability/Accessibility**: being able to be stored alongside the code in
  the GitHub repository would be a huge upside since it's the main point of
  collaboration between XebiKart teams.
- **Strong structure definition**: most of the ADRs will be writtent
  collaboratively. Having a strong definition of the structure of an ADR would
  help having everyone at the same page.
- The use of tooling such as `adr-tools` is not envisioned and will thus not
  impact the choice

## Considered Options

- [MADR](https://adr.github.io/madr/) - The Markdown Architectural Decision
  Records
- [Michael Nygard's
  template](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)
  - The first incarnation of the term "ADR"
- Other templates listed at
  <https://github.com/joelparkerhenderson/architecture_decision_record>

## Decision Outcome

Chosen option: TBD

## Pros and Cons of the Options

### MADR

Pros:

- The metadata at the beginning are clear and readable
- The more structured approach make it easier for people to get into it
- Markdown is already known by every people who will use these ADRs

Cons:

- Is more complex that Nygard's format, even if it's bearable

### Michael Nygard's template

Pros:

- Less structured so theorically easier to write, at least for a single person

Cons:

- A bit too simple; most ADR seen written with this format so far seem to not
  be complete enough to grasp all the decision factors later on

### Other templates

Other templates were really not really convincing.

## Links

- [_"Architecture et documentation : les
  ADRs"_](https://blog.xebia.fr/2019/03/05/architecture-et-documentation-les-adrs/),
  an excellent blog article in French written by Sylvain Decout from Xebia, has
  been a nice inspiration for this choice
