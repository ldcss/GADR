# Decision Log

Decisions made for this project will be tracked here in as ADRs using the MADR format. Information
about ADRs is available at [adr.github.io](https://adr.github.io/) and information on the MADR format specifically
is available at: [adr.github.io/madr](https://adr.github.io/madr/).

## How to Add an ADR
Install [adr-tools](https://github.com/npryce/adr-tools) and [adr-log](https://github.com/adr/adr-log).

##### 1. Create a new ADR file
Create with the title "Use MySQL Database":

    adr new Use MySQL Database

Create a new ADR that supercedes ADR `#0012`:

    adr new -s 12 Use PostgreSQL Database

Create a new ADR that supercedes ADRs 3 and 4, and amends ADR 5:

    adr new -s 3 -s 4 -l "5:Amends:Amended by" Use Riak CRDTs to cope with scale

<br/>
##### 2. Write the ADR
<br/>

##### 3. Update the ADR log at `decision-log/index.md`

    adr-log -d docs/decision-log/ -i

Or manually update the list.

## Log
This log is the list of decisions made for the RTK Companion project.

<!-- adrlog -- Regenerate the content by using "adr-log -i". You can install it via "npm install -g adr-log" -->

- [ADR-0001](0001-create-an-anki-addon.md) - Create an Anki Addon for RTK
- [ADR-0002](0002-define-goal-for-an-mvp.md) - Define Goal for an MVP
- [ADR-0003](0003-mvp-functionality-in-add-card-window.md) - Different Approach to the MVP

<!-- adrlogstop -->






