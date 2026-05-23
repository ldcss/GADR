# 14. Use GOV.UK Notify for sending notifications

Date: 2018-07-18

## Status

Accepted

## Context

The Data Submission Service will need to send notifications to suppliers at
various stages during the submission process.

The notifications will, for example, include:
- Telling a supplier they have a task to complete
- Telling a supplier that a deadline is approaching
- Telling a supplier that their task is overdue
- Providing a receipt for a submission

Initially, the notifications will be email, but may also need to be SMS based in
future.

To reduce the need for each organisation or service team to build it's own
infrastructure for sending email and SMS based messages, the Government Digital
Service (GDS) has built [GOV.UK Notify][service-notify].

GOV.UK Notify can send notifications either via an API call, or by uploading a
CSV to the website. Sending email is free.

The service is already used in various parts of CCS.

## Decision

We will use GOV.UK notify to send notifications for Data Submission Service.

For MVP we may use the CSV upload function to send notifications, but this will
be replaced by automated API calls later in development.

## Consequences

We will set up a GOV.UK Notify account, and configure the appropriate message
templates.

The GOV.UK Notify account will need to be maintained as part of the future
operation of the Data Submission Service.

[service-notify]: https://www.gov.uk/notify
