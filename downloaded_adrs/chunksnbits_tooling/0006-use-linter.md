# Use linter for keeping code well formatted

* Date: 2019-01-01

## Context and Problem Statement

JavaScript / TypeScript code should be well formatted and follow agreed on coding guidelines.
There should a defined set of coding guidelines the developers involved in the project agree on in project initialization phase.
The coding guidelines are never to be considered final and can be fine-tuned if necessary in any project phase.

## Considered Options

* tool supported by using [tslint](https://palantir.github.io/tslint/)
* tool supported by using [prettier](https://github.com/prettier/prettier)

## Choosen Option

Use [tslint](https://github.com/conventional-changelog/standard-version) for linting

**Reasons**

* linting is a [well established standard](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2018-results#js-linters) in the developer community
* TSLint seems to be the most mature linting tool available at this point and is compatible with [pure JavaScript projects as well](https://github.com/Microsoft/vscode-tslint/pull/120)
* Allows to automates the code formatting process (check to [--fix option](https://palantir.github.io/tslint/usage/cli/))
* manual determination of next version possible through `--release-as <major|minor|patch>` command line option is possible

**Notes**

* should be either integrated into either git-commit cycle (`commit` or `push`) or automated in the build stage of the CI
* Manual linting is made available via package script, i.e.:

```shell
yarn lint
```

and by default includes the `--fix` option.

* The default configuration follows the [tslint:recommended](https://github.com/palantir/tslint/blob/master/src/configs/recommended.ts) rule set with those extensions:

| Rule Name  | Setting |
| ------------- | ------------- |
| [quotemark](https://palantir.github.io/tslint/rules/quotemark/) | [true, "single"] |
| [indent](https://palantir.github.io/tslint/rules/indent/) | [true, "spaces", 2] |
| [interface-name](https://palantir.github.io/tslint/rules/interface-name/) | false |
| [ordered-imports](https://palantir.github.io/tslint/rules/interface-name/) | false |
| [object-literal-sort-keys](https://palantir.github.io/tslint/rules/interface-name/) | false |
| [no-consecutive-blank-lines](https://palantir.github.io/tslint/rules/interface-name/) | false |
| [arrow-parens](https://palantir.github.io/tslint/rules/interface-name/) | [true, "ban-single-arg-parens"] |

## Background information
### standard-version

* [tslint](https://github.com/conventional-changelog/standard-version)
* based on [conventional commits](https://conventionalcommits.org/) (which in turn is based on [semantic versioning](https://semver.org/) standard)
