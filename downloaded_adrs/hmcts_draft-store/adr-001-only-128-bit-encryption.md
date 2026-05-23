# ADR 001: Only use 128 bit encryption key length

## Context
Data persisted by the draft-store service needs to be encrypted. No firm steer has been given on the exact level of encryption so latest industry best practice is to be applied.

256 bit keys were attempted, however, to enable 256 bit encryption, the [JCE Unlimited Strength Jurisdiction Policy](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html) files must be installed into the JRE. Without them the maximum length supported in Java is 128 bit.
 
Bruce Schneier says:
> “for new applications I suggest that people don’t use AES-256. AES-128 provides more than enough security margin for the foreseeable future. But if you’re already using AES-256, there’s no reason to change.”

This was based on research conducted in 2009, however, thinking around this is hasn't changed drastically since.

## Decision
We will implement 128 bit length keys using AES encryption and monitor the latest thinking on AES encryption to potentially update our approach in the future.

## Status 
Accepted

## Consequences
Using only 128 bit length keys sounds less than ideal to people at face value so it's important to reference this decision to educate them why we are not using 256. We must also keep up to date with advances in encryption technology to ensure our citizens data remains secure.
