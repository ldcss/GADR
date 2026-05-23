# 6. Use product prefixes for project naming, if necessary

Date: 2019-12-06

## Status

Proposed

## [Context](https://docs.google.com/document/d/1ayJlohp2-s49c1_oypDE1bAfgYa5shR0I1GM6KRzDNA/edit)

Libero projects may span a single product or possibly more, but they live in a single namespace of the [Libero Github organization](https://github.com/libero). Hence the projects need to:

- be attributable to the originating product
- avoid clashes in naming (e.g. many `article-store` projects)

## Decisions

- Name repositories that cover multiple products without prefixes (e.g. `infrastructure`, `community`)
- Name internal and/or product-specific repositories with prefix for specific product (e.g. `reviewer-submission`, `my-product-storybook`)
- Name generic repositories with no prefix (e.g. `media-type`)
- Name forked repositories with the original name, no matter how bad (e.g. [`elifelibero-avada-child-theme`](https://github.com/libero/elifelibero-avada-child-theme), [`texture`](https://github.com/libero/texture))
- Name Docker images following Github repository names (e.g. [`reviewer-submission`](https://hub.docker.com/r/liberoadmin/reviewer-submission))
- Name NPM packages using `@libero` followed by Github repository names (e.g. [`@libero/event-bus`](https://www.npmjs.com/package/@libero/event-bus)

## Consequences

Generic naming makes no assumption about intended reuse, as a repository could be named `my-library` and either be built for reuse and reused, or not be intended for reuse at all.

Docker images and NPM packages should be easily traced back to Github source code.

No long-term direction on the Docker Hub organization to use exists yet.
