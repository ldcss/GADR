
# Use commitizen and commitlint for git commits

* Date: 2018-06-19

## Context and Problem Statement

There is no fully agreed on consensus on how to write commit messages.
This often leads to a big variety of commit message formats used in a project, depending on the backgrounds of the developers involved

## Considered Options

* Do not give a recommendation on commit messages
* Document a standard (e.g., based on https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53), without additional tooling

## Choosen Option

Title and details about possible mutations on the choosen option

**Reasons**

I decided to recommend a commit message format supported by tooling, because:

* it removes questions / options for developers and thus in the long run makes commiting easier
* the chosen format uses the same format backed by companies like [Google](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit)
* it integrates well with other tools like [standard-version](https://github.com/conventional-changelog/standard-version)
* the available tooling supports the onboarding process by giving a command line tool to guide you through format definitions or more complex commits

**Notes**

* Use `npm run commit` / `yarn commit` to allow the [cli-tool](https://github.com/commitizen/cz-cli) help you compile a commit
* [cz-customizable](https://github.com/leonardoanalista/cz-customizable) allows for additional customization options
* There are no predefined scopes other than `system`, which should be used for general `chore` tasks - define scopes based on the module or component mostly effected by the commit
* [commitlint](https://github.com/marionebl/commitlint) including plugins has been added to ensure the commit format
* Configuration settings have been added to [package.json](../../package.json)
* The format for the commit messages is defined in [.cz-config.js](../../.cz-config.js)
* integration has been added using [husky git commit hooks](0002-use-husky-for-git-hooks.md)

## Background information

### commitizen

* [commitizen](https://github.com/commitizen/cz-cli)
* [commitlint](https://github.com/marionebl/commitlint)
* [Angular commit message guidelines](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit)

```shell
git commit -m "type(module-name): imperative, present tense description of commit #ticket"

## example
git commit -m "feat(button): adds button component #pr-123"
```

* Available types
  - feat: describes a product feature added by this commit as well as detectable improvements made to existing modules or components
  - fix: describes a bugfix, i.e., some correction to an existing module or component
  - docs: describes a commit purely for documentation purposes
  - style: describes changes that do not effect the functionality of the code, e.g., linting or code style improvements
  - refactor: describes a refactoring of existing code
  - chore: describes changes made to the infrastructure of the project, e.g., configuration or build jobs
  - revert: reverts a previous commit
  - test: a commit purely to for testing purposes without functional impact
