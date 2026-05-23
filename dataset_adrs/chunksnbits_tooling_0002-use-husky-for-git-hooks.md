# Use husky for git hooks

* Date: 2018-06-19

## Context and Problem Statement

Handling and applying git hooks is a common tasks in most projects.
Keeping the handling (esp. installation) of git hooks is however mosten an complicated matter.

## Considered Options

* do not add tooling for supporting git hooks
* provide a custom node script + templates for installing hooks
* use [husky](https://github.com/typicode/husky)
* … <!-- numbers of options can vary -->

## Choosen Option

Use [husky](https://github.com/typicode/husky) for installing and configuring git hooks

**Reasons**

* provides an painless and consistent approach to handling git hooks
* well [documented](https://github.com/typicode/husky/blob/dev/docs.md), adopted and maintained
* easily configurable

## Background information

### husky

[example | description | pointer to more information | …] <!-- optional -->

* [husky](https://github.com/typicode/husky)
* configuration example

```json
{
  "husky": {
    "hooks": {
      "commit-msg": "npm run commitlint",
      "push": "npm run lint"
    }
  }
}
```
