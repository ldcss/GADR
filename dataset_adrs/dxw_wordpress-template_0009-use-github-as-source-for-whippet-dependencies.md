# 9. Use GitHub as source for Whippet dependencies

Date: 2022-09-06

## Status

Accepted

## Context

We are migrating all our project repos from GitLab to GitHub. Doing the same with our Whippet dependency repos (mainly plugins, but could also be themes) will eventually mean we no longer have to maintain our GitLab instance, and will facilitate automation of Whippet updates.

## Decision

We should use `git@github.com/dxw-wordpress-plugins/` as the primary source for third-party plugins. Any custom dxw plugins should be in public repos in `git@github.com/dxw/`.

## Consequences

The `dxw-dalmatian` and `dxw-dalmatian-2` accounts will need access to all repos we reference in `whippet.json` files. They already have access to all repos in `git@github.com/dxw-wordpress-plugins`. If there are any plugin or theme repos in `git@github.com/dxw` which cannot be made public and are referenced in `whippet.json` files, the dalmatian accounts will need to be added to those repos.

All site repos will need to be updated so their `whippet.json` file uses GitHub as the source for all plugins and themes.

We should ensure all documentation is up to date, both in terms of managing Whippet dependencies, and adding new starters/removing leavers from the GovPress team on `github.com/dxw-wordpress-plugins`
