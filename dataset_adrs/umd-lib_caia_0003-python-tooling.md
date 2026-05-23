# 0003 - Python Tooling

Date: May 12, 2020

## Context

Any application exists within a language ecosystem made up of various tools
to perform such tasks as:

* Testing
* Code styling
* Dependency management

Ideally, an application will be largely independent of particular tools, as that
preserves the greatest flexibility in adopting better tools as they become
available.

However, it is also helpful to provide step-by-step instructions for setting up
a development environment suitable for the application. Specific instructions
require at least the mention of particular tools.

## Decision

For documentation purposes, the following tools will used:

* pytest - [https://docs.pytest.org/en/latest/](https://docs.pytest.org/en/latest/)
* pycodestyle - [https://pypi.org/project/pycodestyle/](https://pypi.org/project/pycodestyle/)
* pyenv/pyenv-virtualenv - [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)/[https://github.com/pyenv/pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

Of these, the most controversial is likely to be the use of
pyenv/pyenv-virtualenv for creating virtual environments. Other tools considered
were "venv" and "virtualenv". The main factor in using "pyenv" was its ability
to easily handle multiple Python installations. This, in conjunction, with
"pyenv-virtualenv" makes it easier to create isolated Python environments.

Robust Python environment isolation is important because we have multiple 
Pyhton applications, using different Python versions and dependencies, and need
to enable developers to easily switch between them.

This tooling decision is largely limited to documentation. If a developer wants
to use different tools, which can achieve the same effect, they should be
allowed to do so. The main intention of this decision is to enable step-by-step
documentation of application processes to be able to assume the use of
particular tools, and to demonstrate at least *one* way of performing a task.

## Consequences

The highlighting of particular tools in the documentation causes controversy, as
some developers may feel some other tool is superior for a particular task. The
intention, however, is not to constrain developers to particular tools, but
to enable clearer documentation by providing precise step-by-step instructions.

A developer should be allowed/encouraged to use any tool, as needed. As
tools develop and best practices are modified, the tools used by the application
should also be open to modification.
