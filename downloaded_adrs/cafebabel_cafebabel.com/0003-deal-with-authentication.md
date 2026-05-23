# 3. Deal with authentication

Date: 2017-11-02

## Status

Accepted

## Context

We need user to be able to register, login, retrieve their lost password and so on.

## Decision

After testing Flask-Login which was too limited, we went for Flask-Security
which relies on it but is more complete, as a glue across other Flask extensions.

## Consequences

This is a strong dependency and we have to respect their conventions
and limitations, especially on the ORM side.

Plus, we have to configure an email sending server.
