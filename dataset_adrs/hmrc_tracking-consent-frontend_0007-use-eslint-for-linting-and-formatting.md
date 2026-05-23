# Use eslint for linting and formatting javascript

* Status: accepted
* Date: 2020-12-03

## Context and Problem Statement

We found that without a standardised format our javascript files ended up with different
formats in different files or even multiple formats in the same file.  We also found that
our IDEs had different configurations which meant that using an autoformat tool would give
different results when each of us do it.

## Decision Drivers

* We wanted to spend less time doing manual formatting
* We wanted to spend less time undoing autoformatting which had been applied to unchanged lines
* We wanted to see easily which lines had actually changed when reviewing PRs
* We wanted to avoid discussions about individual's preferences for particular 

## Considered Options

* StandardJS - this is the tool GDS use and we've historically used that on some repos
* Prettier - an opinionated code formatter
* ESLint - a tool we haven't used before in this team but is widely used and widely supported and is highly customisable
* ESLint + Airbnb - using Airbnb's style as a rule set would mean we don't have to decide between the many different
  configuration options available
* ESLint + Prettier + Airbnb - Both ESLint and Prettier have Airbnb setups and can be used simultaniously

## Decision Outcome

Chosen option: ESLint + Airbnb

We decided to use ESLint with Airbnb because the Airbnb approach is [well documented](https://github.com/airbnb/javascript)
and adopting this meant we wouldn't have to make each decision ourselves.  We decided not to use Prettier as well, there 
was a discussion about the possibility of conflicting format changes between the two tools - we encountered one of these,
it was overcome with config updates.

ESLint is compatible with both Javascript and Typescript projects which made it seem particularly suitable for us as we
chose to use Typescript for Tracking Consent but we usually use Javascript.

Each of the current team members use JetBrains IDEs and that has a built-in plugin which supports auto formatting on save,
this is also a common feature which most IDEs have.

We decided to add pre-commit and pre-push hooks which ensure that the style rules have been met but do not mutate code.
We discussed the option of formatting the code on commit but we felt that this introduced an uncertainty about what we
were committing.

### Positive Consequences

* Code style within a file will be consistent 
* Files within a project will be consistent with each other
* When widely applied this Javascript/Typescript files between projects will be consistent
* IDE will reformat for us which takes away the need for us to do it ourselves
* Code reviews will focus less on code format and more on the details of the changes made
* Builds will fail if format isn't followed which guarentees consistency

### Negative Consequences

* Builds will fail if format isn't followed which can disrupt focus/workflow (mitigated by pre-commit hooks)
