# Use data attribute for specifying tracking consent banner language

* Status: accepted
* Date: 2020-11-16

## Context and Problem Statement

Tracking consent reads the PLAY_LANG cookie to determine whether to render the banner in Welsh. PLAY_LANG is the cookie
used by the Play Framework to persist a user's language preferences. It will be set to 'cy'
when a user has selected Welsh using the language toggle in MDTP services using the Play Framework.

Teams are increasingly setting PLAY_LANG to HttpOnly in an attempt to get green ZAP tests, even though there are no
known security concerns around keeping PLAY_LANG as a normal cookie. Setting a cookie to 
HttpOnly makes it unreadable within the client-side Javascript code that renders the tracking consent banner. The result
 of this is that the banner will not be translated into Welsh for these services.

A related issue is that PLAY_LANG is not set for classic services written in Java, which means a Welsh version of the banner is not 
currently available for classic services.

It is worth noting that the only other known instance of our reading PLAY_LANG using Javascript is in the assets-frontend
[timeout dialog](https://github.com/hmrc/assets-frontend/blob/97c638289e23bee255ac30724a8572c6efa96817/assets/patterns/help-users-when-we-time-them-out-of-a-service/timeoutDialog.js#L14) timeout dialog. All the new govuk-frontend and hmrc-frontend components use data attributes instead.

Should we remove the reading of PLAY_LANG in tracking consent and accept a data-language attribute instead?

## Decision Drivers

* The need to support classic services
* The time-sensitive nature of this issue. The need to deploy quickly before too many services have integrated, to 
avoid services having to upgrade a second time.
* The preference for avoiding further changes to tracking consent. This is a non-breaking change.
* The preference for not advising teams to add exemptions to ZAP tests across MDTP
* The preference for consistency in language settings across our frontend components

## Considered Options

* Do nothing
* Re-work to use data-language instead of PLAY_LANG

## Decision Outcome

Chosen option: "Re-work" because we need to act now and in the medium term we are not in a position to uncouple services' 
dependency on PLAY_LANG nor add a global exemption for PLAY_LANG into Zap tests. We also agreed that our frontend 
components should be consistent in their treatment of language until such time as we are able to provide an 
alternative approach that works for all components.

### Positive Consequences

* Classic services or services using other non-Scala or non-Play frameworks can get Welsh translations for the banner
* Services do not need to set any HttpOnly exemptions in their ZAP tests, which may mask other legitimate warnings/errors
* Language setting is consistent with other components e.g. hmrcTimeoutDialog, hmrcReportATechnicalProblem etc

### Negative Consequences

* We will need to make a small change to tracking consent and communicate this change to teams
* Teams will need to upgrade to the latest version of play-ui/play-frontend-hmrc to get language translations
* Teams not using the tracking consent helpers will need to add a data-attribute for the language
