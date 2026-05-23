# Architectural Decision Records
We use [Markdown Architectural Decision Records](https://adr.github.io/madr/) to document our design choices. We support the use of relevant tooling,
but we do not require their use.

## Context and Problem Statement
- How should we document design choices? 
- Should we use tooling?

## Decision Drivers
* Project is under documented
* The project has no dedicated team: Contributors are temporary and have varying backgrounds
* Existing choices prove hard to fathom. 

## Considered Options
* Status quo / Git blame
* Confluence
* Various ADR-templates

## Decision Outcome
Chosen to use architectural decision records using the MADR-template, because
- The project needs a structural way conserve history. 
- ADRs live inside the codebase.
- ADRs provide little overhead.

Chosen MADR over other templates, because:
- ticks all boxes
- no additional cruft
- nice balance between simple and complete
- adds <optional> modifiers to help guide writing
- most recently maintained.

Chosen to leave tooling optional, because:
- It can provide convenience 
- It doesn't force stringent practices
- Creating and maintaining ARDs manually is simple enough

## Pros and Cons of the Options

### Status Quo
* (+) No maintenance cost.
* (-) Information loss
* (-) risk of undoing choices/ re-introducing resolved bugs
* (-) project becomes hard to grasp for new members 

### Wiki
* (+) Easy format
* (+) Outside codebase, so available to non-technical stakeholders
* (-) Technical decisions are hardly ever of interest to non-techs
* (-) More complex than ADR
* (-) Outside codebase, so difficult to keep in sync.  

### Architectural Decision Records
* (+) Simple to create 
* (+) Easy to maintain
* (+) Close to code; committed together with relevant changes
* (+) No additional systems required
* (-) Upcoming; external forms are more common and better known.
* (-) Hard to reach for non-technicals

We considered the templates using the following criteria:
* Must have
    - Easy to create
    - short and compact
    - clear
    - publishable format (such as .md)
    - considers alternatives
    - stripping superfluous options > adding missing options
        - maintains consistency
        - stripping is easier
* nice to have
    - auto publish
    - build integration
    - wiki/confluence/... integration
    
Templates rejected:
- ADR template by Michael Nygard (simple and popular)
    - (+) short sweet & simple
    - (-) Too short. No versioning, No alternatives.  
- ADR template for Alexandrian pattern (simple with context specifics)
    - (+) complete
    - (-) too formal  
- ADR template for business case (more MBA-oriented, with costs, SWOT, and more opinions)  
    - (-) way too formal  
- ADR template using Planguage (more quality assurance oriented)  
    - (-) way too formal  
- ADR template by Jeff Tyree and Art Akerman (more sophisticated)  
    - (-) way too formal  

### Further info
- can tooling be optional?  
Yes. Copy template manually. Update index manually.
- Can templates be customized (stripped/added to)?  
Yes. MD template is not final.
- Use tooling.  
Yes, but optional. Tooling is not required, but adds convenience.

## Links 
- [MADR](https://adr.github.io/madr/)  
- [Collection of different ADR types](https://github.com/joelparkerhenderson/architecture_decision_record#adr-file-name-conventions)  
- [Tooling](https://github.com/adr/adr-tools/)  
- [More tooling](https://github.com/adr/adr-tools/blob/patch-1/INSTALL.md)  
- [Yet more tooling](https://github.com/npryce/adr-tools)  
