# 3. Use poetry for dependency management

Date: 2020-02-26

## Status

Accepted

## Context

Python projects should use virtualenvs to isolate them from the system Python. In addition, it is useful
to use a tool to manage dependencies installed in that virtualenv. There are a number of options in this
space, and the Python community has not landed on a single standard. Each project needs to select which
tools to use, usually a selection of tools that integrate well.

The Python Package Authority usually recommends Pipenv, but it has several problems that are not being
dealt with for various reasons. A newcomer in the space is Poetry, which has a bit of a following, and
claims to support the use case well. It is also following the new pyproject.toml standard.

## Decision

We will use Poetry for this project. (https://python-poetry.org/)

## Consequences

Developers working on Kafkarator needs to be familiar with Poetry, and how to use it.

