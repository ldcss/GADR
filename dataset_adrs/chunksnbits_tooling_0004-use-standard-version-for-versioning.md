# Use standard-version for versioning

* Date: 2018-06-19

## Context and Problem Statement

There needs to be a well defined approach to versioning within a project or library.
The current version (and next version) should be easily comprehensible to everyone (new) in a project.
The changes made from version to version should be traceable, both in code and from a business perspective

## Considered Options

* manual handling using custom versioning
* manual handling using [semantic versioning](https://semver.org/)
* tool supported handling using custom scripting
* tool supported handling using [standard-version](https://github.com/conventional-changelog/standard-version)

## Choosen Option

Use [standard-version](https://github.com/conventional-changelog/standard-version) for versioning

**Reasons**

* follows [semantic versioning](https://semver.org/) standard
* Easy (automatic) versioning of your application or library, including automatic changelog updates
* manual determination of next version possible through `--release-as <major|minor|patch>` command line option is possible

**Notes**

* dependencies and `script` configuration has been added to [package.json](../../package.json)
* to create a new release run:

```shell
yarn release # alternatively: npm run release
```

* run `yarn release` to create a new version. This will
  - update the `version` field in [package.json](../../package.json)
  - update the changelog
  - create a commit (including commitmessage following standard defined defined in [ADR-0003](0003-use-commitizen-commitlint.md))
  - create a new tag for the commit
  - synchroniye commit with `remote`
* versions will be detected automatically from those commit message types:
  - `fix` will result in a `patch` version bump
  - `feat` will result in a `minor` version bump
  - adding `BREAKING CHANGE: <description of breaking change>` will result in a `major` version bump
* for applications (that usually do not create breaking changes) use `--release-as <major|minor|patch>` to force a `major` bump

## Background information

### standard-version

* [standard-version](https://github.com/conventional-changelog/standard-version)
* based on [conventional commits](https://conventionalcommits.org/) (which in turn is based on [semantic versioning](https://semver.org/) standard)
