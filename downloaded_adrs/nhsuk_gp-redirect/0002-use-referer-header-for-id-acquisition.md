# 2. Use referer header for ID acquisition

Date: 2017-06-21

## Status

Accepted

## Context

The mechanism for directing people to the new GP Profile pages is to use an
existing system where a banner is displayed on the current page. From this
banner the user is able to confirm they wish to see the new page by clicking on
a button. The button is a link, able to be configured for a single static URL.

The user needs to experience a seamless transition to the new page after they
have clicked on the button. In order to do this the ID of the previous page
is required. Given the constraints of the existing system the `referer` header
is the only way that can be determined.

## Decision

We will use the `referer` header to identify the ID of the GP profile page the
user was previously viewing in order to redirect them to the new page.

## Consequences

If the `referer` is unavailable the ID of the GP will not be able to be
determined and a `Page not found` page will be displayed.
Situations where no `referer` is available include:
* Browsers configured to block the transmission of `referer` headers
* Some versions of
  [IE](https://support.microsoft.com/en-us/help/178066/info-internet-explorer-does-not-send-referer-header-in-unsecured-situations)
