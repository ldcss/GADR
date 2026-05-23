# Supported Python Versions

Date: 2017-11-20

## Status

Superseded by [0009-supported-python-versions-containers](adr/0009-supported-python-versions-containers.md)

## Context 

eLife has numerous projects written completely and partly with the [Python programming language](https://www.python.org/).

In order to provide language version consistency across projects we need to get a consensus on which versions we are going to support. 

We have only gone up to Python 3.5 due to the default Python versions pre installed on the Ubuntu distributions we use.

## Decision

We will use Python >=2.7.14 as our default version for any project that solely uses or supports Python 2.

We will use Python 3.5 as our default supported version for any project that solely uses or supports Python 3.

## Consequences

Any libraries that are currently only supporting Python 2 are to be upgraded to support both Python 2 & 3.

Any projects that are currently using Python 2 are to be upgraded to Python 3.

All Python 2 support in our libraries will remain until official support is dropped in 2020.

