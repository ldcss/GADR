# 0011 - Pin "mbtest" library to v2.5.1

Date: March 26, 2021

## Context

On March 22, 2021, it was discovered that the "caia" Jenkins builds were
failing. All the failing tests were failing with the following error, related
to a "get_actual_requests" method call:

```
TypeError: 'generator' object is not subscriptable
```

The "caia" build was last successful in Jenkins on October 7, 2020. No builds
were performed again until March 22, 2021, as there was no development work
being done on the project.

Builds were made on March 22, 2021 because of a move to the
"GitHub organization" pipeline in LIBITD-1880, which triggered rebuilds in all
existing projects.

When the last successful build was made in October, the "mbtest" library
([https://github.com/brunns/mbtest](mbtest)) was at v2.5.1. In v2.5.2, the
"src/mbtest/server.py" file was modified, changing the "get_actual_requests"
method signature (see [this commit e398f2f1f32420](mbtest_commit)). from:

```
def get_actual_requests(self) -> Mapping[int, JsonStructure]:
```

to

```
def get_actual_requests(self) -> Iterable[Request]:
```

The change from a Mapping to an Iterable is the cause of the error in the tests.

## Decision

The simplest solution for the moment is to "pin" the version of the "mbtest"
library to v2.5.1 in the "setup.py" file. This will preserve the current
behavior, until further "caia" development warrants additional testing.

## Consequences

This decision improves the stability of the "caia" builds by pinning the
"mbtest" dependency to a specific version. Since this library is only used
for testing, keeping up with the latest updates (i.e. for security fixes) is
not a concern.

If significant additional development of the "caia" project is performed, it
would likely be worthwhile to update to the lastest "mbtest" version, and update
the tests appropriately.

[mbtest]: https://github.com/brunns/mbtest
[mbtest_commit]: https://github.com/brunns/mbtest/commit/e398f2f1f324209500506cc72fa0a045b2d420f4#diff-f6d8bc80c4ba5a033a4d011f675c4b43767a86fcd51b4463bdad275911ef95b6L159-R161
