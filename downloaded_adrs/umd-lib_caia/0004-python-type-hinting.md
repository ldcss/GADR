# 0004 - Python Type Hinting

Date: May 14, 2020

## Context

Python is a dynamically typed language and does not require the explicit
declaration of types as in languages requiring static typing, such as Java.

Python 3.5 and later support "type hinting" as described in
[PEP 484](https://www.python.org/dev/peps/pep-0484/). A useful tutorial is
[https://realpython.com/python-type-checking/](https://realpython.com/python-type-checking/).

Type hinting does not affect runtime behavior, it is simply a guide for
developers and IDEs as to what types are expected.


## Decision

Providing some indication of the expected type for method parameters and return
types seems useful for documentation purposes. This is especially true for
applications that are not under continuous development, and may be
maintained/extended by developers other than the original authors. 

Therefore, type hinting should be used where possible. Developers should not
make extraordinary efforts to provide type hints.

## Consequences

As type hinting does not affect the runtime performance of Python, there should
be no risk to behavior of the application.

Type hinting is expected to add only a small burden to developers during
development. It is expected that the time spent will be more than offset
by the documentation benefits that type hinting provides.
