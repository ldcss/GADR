# 1. Login API Choice

Date: 2019-04-09

## Status

Accepted 

## Context

It would be convenient to use the Google Login API as an alternative method for users to login. This would provide a template for our own login details stored in the DB, as well as a quick way to get the Sprint 1 User story related to login completed ASAP. 

## Decision

Using a well known and widely known/supported login mechanism such as Google's OAuth2 will allow more rapid development of an appropriate security setup for the site. We will apply for an API key and start implementing the login/registration page through the Google Login API

## Consequences

We don;t want users to be required to have a gmail account. Therefore we _still_ have to build a normal login/password authentication setup, in addition to the google login, and with additiona checks to confirm the interoprability between the two registration/login methods. However, the speed in the first sprint, and leaning on established beats practice from a major and knowledgeable company such as Google means we can learn how to best structure the data stored/required for our own site login.

 * Additional testing on interoperability
 * The password and user details have a security context and must be labelled as such
