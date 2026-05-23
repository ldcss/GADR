# Supported PHP Versions

Date: 2017-12-20

## Status

Proposed

## Context 

eLife has several microservices (and larger projects) written in PHP.

In order to provide language version consistency across projects we need to get a consensus on which versions we are going to support. 

There is an exception, `crm` not being upgraded on PHP 7 (using 5.6 instead) but supporting it.

Staying up to date with the major and minor versions of PHP is important:

- to be able to use new features and libraries (nice to have)
- to keep working on a version that receives bug fixes and security updates (must have)

All infrastructure is currently based on:

- Ubuntu 14.04 (doesn't have PHP 7.x by default)
- Ubuntu 16.04 (does have PHP 7.0 by default)
- a popular [PPA](https://launchpad.net/~ondrej/+archive/ubuntu/php) filling in the blanks, supporting 7.0, 7.1, and 7.2.
- official [PHP Docker images](https://hub.docker.com/_/php/) supporting 5.6, 7.0, 7.1, and 7.2.

PHP 7.0 has ceased active support, but has [security support](http://php.net/supported-versions.php) until 2018-12-03.

## Decision

We will use PHP 7.0 on all existing and new PHP projects bar exceptions that do not support it (`crm` if needed).

We will upgrade to PHP 7.1, PHP 7.2 and similar minor versions as a concerted effort on all libraries and projects, before the end of the security support.

## Consequences

No libraries or projects should require PHP >= 7.1 until it is provided by:

- an approved builder-base-formula state such as `elife/php71.sls`, if the project is using EC2 instances anywhere
- a base image such as `elife/php:7.1` derived from the official ones, if the project is using containers anywhere

A single epic should capture all the necessary upgrades when we decide to do the switch to a new minor version.
