# 6. Use Roave/SecurityAdvisories to help protect against vulnerable packages

Date: 2021-07-13

## Status

Accepted

## Context

We often use third-party Composer packages in our themes. We should review these packages via [libraries.io](https://libraries.io/) before installing them, and should receive GitHub security alerts on repos using composer packages that have known vulnerabilities.

However, Composer does not warn you if you're installing a package that has a known vulnerability - those warnings will, at best, only come after that change has been pushed up to GitHub.

## Decision

Add the [Roave/SecurityAdvisories](https://github.com/Roave/SecurityAdvisories) package to our template theme as a Composer dev dependency. 

This package does not contain any executable code, it just contains a `composer.json` that uses Composer's `conflict` setting to provide a list of versions of Composer packages with known vulnerabilities. Attempting to install one of the listed packages at a known vulnerable version will result in an error, preventing the package being installed.

The SecurityAdvisories package takes its list of known vulnerabilities from [FriendOfPHP/security-advisories](https://github.com/FriendsOfPHP/security-advisories) and [the GitHub Advisory Database](https://github.com/advisories?query=ecosystem%3Acomposer), and is updated regularly.

## Consequences

Whilst we should still do manual review of new dependencies, as per [Tech Team RFC 087](https://github.com/dxw/tech-team-rfcs/blob/main/rfc-087-use-libraries-where-possible.md), this will provide us with an additional layer of protection against potential vulnerabilities.

SecurityAdvisories will only throw errors when running `composer update` or adding a new dependency via `composer require`, so it should be noted that any warnings will not automatically be generated.
