# ADR 4: Tokenization and Static Assets

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

Tokens have a significant role in theming. They're responsible for defining the primitives of our theme, such as color codes, font names, and others. Tokens are relevant to determining asset locations too.

We must find a proper way to handle and maintain our tokens.

## Decision

We've decided to use [Style Dictionary](https://amzn.github.io/style-dictionary/#/) as our framework to handle tokens. It is easy to use since we can define our tickets in standard JSON but empowering them with string interpolation, variables, and other features.

For our static assets, we're going to host them at [AWS S3](https://aws.amazon.com/s3/), defining the proper CORS rules, and refer the location of those as tokens for our applications to use.

Instead of increasing the size of our Javascript bundle with static assets, we prefer to keep it simple and light by hosting those in an S3 bucket and asking for the application to download it.

## Status

**DEPRECATED** _check [update 1](#update-1)_

## Consequences

Tokenization is a complex process. We need to look out and keep it simple. The logic (like mapping those tokens to theme properties) must happen in the design-system itself, keeping the token package just for constant's definition.

---

## More reading

* [Style Dictionary's docs](https://amzn.github.io/style-dictionary/#/)

## Updates

### Update 1

After [business/ADR#001](https://github.com/budproj/architecture-decision-log/blob/main/records/business/001-reducing-initial-technical-complexity.md), we've decided to stop the development of a decoupled design system.
