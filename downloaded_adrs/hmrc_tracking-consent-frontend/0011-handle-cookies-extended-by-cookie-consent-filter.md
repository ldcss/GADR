# Handle cookies extended by CookieConsentFilter

* Status: accepted 
* Date: 2025-04-22

Technical Story: PLATUI-3628

## Context and Problem Statement

To fix an issue with `userConsent` and `mdtpurr` cookies being set to `httpOnly` due to a bug in bas-gateway signout, a 
filter was added to `tracking-consent-frontend` to create new non-`httpOnly` versions of these cookies. However, these were
created with `maxAge` set to the original `maxAge`, meaning existing `userConsent` / `mdtpurr` cookies were essentially **extended**
by `maxAge`.

## Decision Drivers

* Is it an issue that some users have had their `userConsent` and `mdtpurr` cookies extended by 1 year (`maxAge` as set in code)?
* Which cookie is set in which library or service?
* What is GDPR legislation on this?
* If it is an issue, what technical solutions do we have in `tracking-consent-frontend`?
* What are effects on other parts of MDTP if currently cookies are invalidated by updating the service version?

## Considered Options

* Option 1: Do nothing
* Option 2: Invalidate all existing `userConsent` cookies by incrementing the cookie version

## Decision Outcome

Chosen option: "Option 2: Invalidate all existing `userConsent` cookies by incrementing the cookie version", because we
clearly state in our page https://www.tax.service.gov.uk/help/cookie-details that the expiry of `userConsent` is 1 year,
and there may be a significant number of end users where that isn't correct. By choosing this option, the negative impact
is shifted to within HMRC, rather than impacting end users and potentially contravening GDPR legislation by knowingly having
incorrect cookie duration.

This work will be done as a separate ticket, as we will want to let other teams know before we invalidate the `userConsent`
cookie.

## Pros and Cons of the Options

### Option 1: Do nothing

* Good, because in UK legislation there is **not** a maximum duration of persistent cookies (see https://gdpr.eu/cookies/, 
  "ePrivacy Regulation"), so cookies lasting 364 days + 1 year would not be contravening UK GDPR legislation)
* Good, because this would not invalidate `userConsent` cookie for **all** users, regardless of whether they have had 
 `userConsent` extended
* Good, because it would not cause the cookie banner to "reappear" for all users
* Good, because no further action required
* Bad, because for a small number of users, the duration of their `userConsent` cookie would  be longer than the 1 year 
  stated here: https://www.tax.service.gov.uk/help/cookie-details

### Option 2: Invalidate all existing `userConsent` cookies by incrementing the cookie version

* Good, because it would ensure that `userConsent` cookies do not exceed the stated duration of 1 year
* Good, because seems straightforward to implement in code
* Bad, because it would effectively invalidate the `userConsent` cookies for all users of tax.service.gov.uk and 
  other domains such as Developer Hub, meaning end users would see the banner again
* Bad, because it would lead to a drop in analytics, definitely in the short term and potentially in the longer term
* Bad, because it would fix the issue for `userConsent` but not `mdtpurr` (`mdtpurr` is set in [hmrc-frontend](https://github.com/hmrc/hmrc-frontend/blob/main/src/components/user-research-banner/user-research-banner.js#L3))
* Bad, because it would require PlatUI to announce to impacted teams such as CIP and experimentation team
