# 3. FCM over GCM

Date: 2017-06-22

## Status

Accepted

## Context

We had to decide on whether to implement Firebase Cloud Messaging (FCM) or
Google Cloud Messaging (GCM), as they both provide push notification support
for Android.

## Decision

We decided to implement FCM (despite there being a fair bit of GCM-related
information available) since, in Google's own words:

> Firebase Cloud Messaging (FCM) is the new version of GCM. It inherits the
> reliable and scalable GCM infrastructure, plus new features! See the FAQ to
> learn more. If you are integrating messaging in a new app, start with FCM.
> GCM users are strongly recommended to upgrade to FCM, in order to benefit
> from new FCM features today and in the future.

We believe that GCM will have a long-tail, but that FCM is the recommended way
to move forward.

## Consequences

The implementation between FCM and GCM is somewhat different, but the
implementation is not going to be overly costly.
