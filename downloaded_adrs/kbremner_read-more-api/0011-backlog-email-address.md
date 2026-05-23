# 11. Backlog Email Address

Date: 2017-10-22

## Status

Rejected

## Context

One of the sources for links that are eventually saved to Pocket are email newsletters. However, a user often does not want to put all
articles from a newsletter in to Pocket. So, newsletters waiting to be reviewed can clutter an email inbox.

A user could be provided with an email address that they could send emails to. Links would then be extracted from a received email
and be added to a backlog. A webpage would need to be provided for users to view this backlog, which could be part of the existing
chrome extension.

Handling inbound email would require the use of a transactional email service, such as MailGun, that can POST to an API endpoint
when an email is received.

The recipient email address, containing a unique identifier associated with a particular user, would be used to determine what list to add
articles to.

A protected account ID in the email address is likely to be too long for users to want to use.

Using an unprotected account ID in the email address for a user would expose the plaintext and cipher, which could make it easier for an
attacker to determine the private key material.

To prevent both of the above issues, a new UUID would need to be generated for use in the email address for a user.

Emails would consist of a variety of formats, which may cause issues in identifying links.

Some links would not be relevant and would need to be removed (i.e. unsubscribe links).

Some emails contain a link to a webpage containing the same content, in case the user's email client is not able to correctly render the
email. This link could be added to Pocket, rather than the links within the email. However, there is not a common format to identifying
this email address.

Other services, such as If This Then That, allow triggers to be setup where links can be added to Pocket when an email is received.

The suggested backlog approach may be viewed as unnecessary by users. It may be easier for them to add to Pocket and filter while
browsing through their list of articles. Linked with the difficulties in parsing emails, this feature could be difficult to implement
and be of little actual use.

## Decision

We will not provide users with an email address they can send emails containing articles to.

## Consequences

Users will have to use an alternative service to perform the extraction of links from an email newsletter.