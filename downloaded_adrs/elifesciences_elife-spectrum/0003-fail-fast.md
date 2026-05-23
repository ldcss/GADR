# 3. Fail fast any given test

Date: 2017-09-15

## Status

Accepted

## Context

A full test suite run may take > 10 minutes. Given a particular failure, at the end2end level we may encounter many different failures as consequences: for example, a missing file in the publication process may lead to errors in downstream services that rely on it.

Many tests also use polling, waiting for a success condition like a 200 response.

## Decision

Fail a test that detects something is wrong as soon as possible, without triggering additional checks or commands on the system under test.

## Consequences

If polling detects an unexpected temporary failure condition, it should fail immediately without waiting. For example, a 500 where only 200 or 404 is allowed.

Some systems allow to detect errors earlier than the timeout, like the dashboard. If the test see *any* error message on the dashboard, they should fail immediately too.
