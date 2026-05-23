# 8. Use a dependabot.yml file to configure security alert rules

Date: 2021-11-10

## Status

Accepted

## Context

GitHub security alerts can provide us with useful information when there is a vulnerability in a package we use.

However, currently the vast majority of alerts we receive are for vulnerabilities in NPM dev dependencies, which are highly unlikely to lead to any real vulnerability in the production environment. See https://overreacted.io/npm-audit-broken-by-design/ for more details.

This creates so many false positives that we're unable to spot the meaningful security alerts we need to act upon amongst the noise.

## Decision

We will use a `dependabot.yml` file to [configure the security alerts](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates) so that alerts are raised for all composer packages, but only production NPM packages. 

## Consequences

This should filter out most of the noise of alerts we don't need to act on, and leave us with a manageable number of meaningful security alerts. It will also control what dependencies Dependabot automatically opens PRs for.

Because Dependabot does not currently allow for glob/wildcard-based rules (see https://github.com/dependabot/dependabot-core/issues/2178), we will need to manually maintain the file for each repo.

A PR template should help ensure we keep the `dependabot.yml` files up to date, and a separate ADR will be opened to that effect.
