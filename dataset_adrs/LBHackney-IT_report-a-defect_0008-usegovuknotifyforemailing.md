# 8. UseGovUkNotifyForEmailing

Date: 2019-06-06

## Status

Accepted

## Context

The issue motivating this decision, and any context that influences or constrains the decision.

This service has a need to send emails and SMS to users. As Hackney is approved as an organisation that can use GOV.UK Notify we are able to use this service and take advantage of the reliability and low costs.

Hackney already use Notify for other services, although it is not yet referenced in their playbook https://github.com/LBHackney-IT/API-Playbook

## Decision

Use Notify over a third party service such as SendGrid for the sending of emails and SMS

## Consequences

Avoids an expensive alternative.

Consistent tooling across Hackney digital services.

Simple and known set up path.
