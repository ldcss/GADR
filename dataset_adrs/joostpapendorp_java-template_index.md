# Architectural Decision Records
Since this is a shared project, many different people will contribute at different times. It is therefor vital to document 
our insights, so future contributors can quickly grasp the meaning of certain choices. For this, we use architectural 
decision records, ADR for short. These records can be found in `/docs/adr/`.  This index provides an 
overview of all the ADRs.  
For more information on contributing, see below.   

### Index

<!-- adrlog -- Regenerate the content by using "adr-log -i". You can install it via "npm install -g adr-log" -->

- [ADR-0000](0000-architectural-decision-records.md) - Architectural Decision Records
- [ADR-0001](0001-test-driven-development.md) - Test Driven Development
- [ADR-0002](0002-hexagonal-architecture.md) - Hexagonal Architecture - Clean Architecture variant
- [ADR-0003](0003-git-branching-model.md) - Use GIT-Flow branching model.

<!-- adrlogstop -->

#### Writing ADRs 
To write a new ADR, copy the [template](./adr/template/xxxx-name-with-dashes.md) from `docs/adr/template` to `docs/adr`.
Rename it, replacing `xxx` with the next 4-digit serial number.  
Fill out the template with the decision. Don't worry too much over style, the most important
thing is that the decision is recorded clearly and concisely.
  
#### Updating the index.
Finally, update the [index](./adr/index.md) with a link to the new ADR. This can be done either manually or using `adr-log`.

#### Tooling
Some tooling is available, most importantly `adr-log`.  

`adr-log` is a tool to automatically update the index of the ADRs. Install `adr-log` via `npm install -g adr-log@2.1.2`. 
You'll need to have  [Node Package Manager](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.  
To run the update, open a shell inside the `docs/adr` directory and run `adr-log -i`

*Note*: 2.1.3 is the latest version of `adr-log`, but it has an open issue which causes the index to contain broken links.
(see https://github.com/adr/adr-log/issues/32)   

Further tooling automates the generation of new ADRs, among other things , and can be found at https://github.com/adr/adr-tools/.
It does require more work to set up. See the instructions at https://github.com/adr/adr-tools/blob/patch-1/INSTALL.md  

#### Further reading
- https://adr.github.io/madr/ for information on our template 
- https://github.com/adr/ for more information on the ecosystem of which our template is but a part.
- https://github.com/adr/adr-tools/ for the tooling
- https://github.com/joelparkerhenderson/architecture_decision_record for more general informatinon and further reading.
