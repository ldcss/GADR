# 7. Detach from Expo

Date: 2018-10-02

## Status

Accepted

## Context

The size for our Android app is 28mb even if it only has 2 screens with simple tabs and lists.
This is because the size for an Expo app on iOS is approximately 33mb (download), and Android is about 20mb because Expo includes a bunch of APIs regardless of whether or not you are using them. Expo will make this customizable in the future but for now, there is no option to customize it.

## Decision

Detach from Expo.

## Consequences

-