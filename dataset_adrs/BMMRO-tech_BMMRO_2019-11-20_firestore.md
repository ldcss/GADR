# Firestore

**Status:** Accepted

## Context

We need a database in order to store the data provided by the user in the different forms.

## Decision

To reduce the amount of integrations and complexity, we've decided to use one of the databases that Firebase offers.
Under the Firebase umbrella are Real-time database and Firestore which are similar in many features.
Google recommends Firestore for new developers, as it is built upon “the successes of Real-time database”. Also, for our purposes, Firestore is a better choice because:

- It offers offline support for iOS, Android and Web clients whereas real-time DB supports only iOS and Android clients.
- The one-big-JSON-tree structure of real-time can become difficult to maintain as the DB grows. Document-based Firestore offers better organisation provisions using collections.
- Scaling on firestore is automatic whereas scaling on real-time database requires sharding.

## Links

- [Differences between the Firestore and Real-time Database](https://firebase.google.com/docs/database/rtdb-vs-firestore)
