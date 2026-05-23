# 1. Title

Date: 2019-05-20

## Status

Accepted

## Context

In order to join a group, a potential member must be invited (it's not correct to add a person to a group without asking permission.) A person invited can either be a member of the website (have an account) or be a new user (no account registered yet). In order to cover both of these scenarios, and to avoid the website being a "walled garden" with a tiny set of users, and to encourage potential future growt, a mechanism to invite users could be an email, sent by an existing member, to any valid email address with an invitation to join. This could be in the form of a token with a payload, or more simply, an extra table in the DB, linking the invited person's email to a trip ID. 

## Decision

The mechanism of an external invitation with a specific link requires the ability to send an email (prefereably attractively  styled and clearly phrased, to avoid being rejected as unsolicited or junk email). The node module 'nodemailer' was selected as appropriate, for its wide support, mature development and ease of use, and 0 dependecies.

## Consequences

Nodemailer adds extra dependecies to node, increasing the number of modules that must be maintained and installed. This is a minor concern. The restrictions that a user must use the same email that they were invited with to login to the website in order to be included in the trip invite that was sent, is a more subtle problem, that can only be migitated by instructing the user in the original email to please use the same email address.

 * Invites must be visible as notifications, or on the Trip Manager page
 * Once rejected, or added, an invite must be removed from the 'invites' table to avoid annoying or confusing the user.
 * MIT license, means high compatibility with existing licenses on other node modules.