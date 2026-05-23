# 8. use-ava-test-runner

Date: 2019-08-27

## Status

2019-08-27 proposed
2019-08-27 rejected

## Context

[Lab][hapi-lab] is misreporting the code coverage stats because I have not set it up to [work with Typescript][lab-ts]. The other issue with Lab is that its community is quite small meaning less plug-and-play with other tools. I thought about using [Ava][ava-typescript] but [this review][dodds-jest] of Ava's performance issues doesn't sound great.

## Decision

Jest seems like the way to go:

- Typescript support
- Large community
- Familiar

## Consequences

- Reconfigure and update tests with Jest

[hapi-lab]: https://github.com/hapijs/lab
[lab-ts]: https://github.com/hapijs/lab#typescript
[ava-typescript]: https://github.com/avajs/ava/blob/master/docs/recipes/typescript.md
[dodds-jest]: https://kentcdodds.com/blog/migrating-to-jest
