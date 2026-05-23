# 4. Separate elife and www-data users

Date: 2018-02-05

## Status

Accepted

## Context

Processes running the application should not be able to modify files in general, as only particular subfolders should be writable, but not the code itself.

It should not be necessary to use `root` privileges to build an application once a folder with the right permissions is available.

Many tools (rightly) also have built-in limitations against running as `root`, or provide flashy red warnings when run as `root`.

Ubuntu Linux distributions provide a standard user `www-data` with UID `33`.

## Decision

Every image should provide a `elife` and a `www-data` user:

- `elife` should be the owner of all the application files.
- `www-data` should be used to run all application containers and any shell executed inside them.

## Consequences

`/srv/` should be property of `elife` which will build applications there.

Compromised `www-data` processes won't be able to rewrite the application code.

No container will be running as `root` or even `elife`.

No shell will be running as `root` or even `elife`.

Non-application containers such as `redis` will usually be run with their own non-root users such as `redis`, `mysql` and so on.
