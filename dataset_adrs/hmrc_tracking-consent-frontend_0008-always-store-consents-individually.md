# Always store consents individually

* Status: accepted
* Date: 2021-03-05

Technical Story: PLATUI-1049

## Context and Problem Statement

tracking-consent-frontend provides a solution for tax users to express their cookie consent preferences via a 
banner and cookie settings page, storing these preferences in a `userConsent` cookie with 
the following structure:

```
{
  version: string, // Currently 2020.1
  datetimeSet: string, // e.g. 2021-03-04T15:16:47.077Z
  preferences: {
    acceptAll?: boolean, e.g. true
    measurement?: boolean,
    settings?: boolean
  }
};
```

The `acceptAll` category was added to allow for future differentiation between users that chose to accept all
via the banner vs users that accepted all by individually selecting 'Use' for each cookie type on the settings page.

We now believe this feature may lead to services assuming the user has consented to the use of types of cookie that
were not actually listed at the point the user consented. For example, if marketing cookies are added in 2022,
is it possible services may assume `acceptAll: true` set in 2021 means that the user has consented to the use of marketing cookies?
Services would need to rely on the cookie version or datetimeSet in order to determine what cookie types
existed at the point the user consented.

Given the need to differentiate between users accepting all cookies via the banner vs the cookie settings is not currently a requirement
should we therefore, remove the acceptAll category and instead set individual categories, so that it is explicit in the userConsent
which categories the user has consented to?

Such a change would result in a new version of the userConsent cookie with the following structure:

```
{
  version: string, // 2021.1
  datetimeSet: string, // e.g. 2021-03-04T15:16:47.077Z
  preferences: {
    measurement?: boolean,
    settings?: boolean
  }
};
```

## Decision Drivers

* the preference for keeping the consenting data model simple, unambiguous and free from duplication
* the need to mitigate the risk of services misinterpreting the preferences stored in the userConsent cookie
* the lack of a current or anticipated future need to differentiate how a user has consented
* that storing preferences individually is consistent with the functionality implemented on GOV.UK (see links below)

## Considered Options

* Remove 'acceptAll' from userConsent
* Do nothing

## Decision Outcome

Chosen option: "Remove 'acceptAll'", because for the reasons above we believe it is the right thing to do and makes sense
 to do before the solution goes live.

### Positive Consequences

* There is less risk user cookie preferences will be misinterpreted by services
* Teams are likely to be less confused and need to ask fewer questions around the meaning of the categories

### Negative Consequences

* The need to increment the userConsent version number and introduce logic for dealing
with old cookie versions.

## Links

* GOV.UK design system [component](https://design-system.service.gov.uk/components/cookie-banner/)
* GOV.UK publishing [documentation](https://docs.publishing.service.gov.uk/manual/cookie-consent-on-govuk.html)
* GOV.UK publishing [component](https://components.publishing.service.gov.uk/component-guide/cookie_banner)
