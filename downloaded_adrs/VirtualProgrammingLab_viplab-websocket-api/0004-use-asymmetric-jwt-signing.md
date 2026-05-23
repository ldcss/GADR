# Use asymmetric JWT signing

* Status: accepted
* Deciders: Leon Kiefer, Per Pascal Seeland
* Date: 2020-05-11

Technical Story: https://github.com/VirtualProgrammingLab/viplab-websocket-api/issues/11

## Context and Problem Statement

When using JSON Web Tokens generating signatures and verifying them is an important task.
JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA.
When implementing JWTs one must decide which method to use.

## Decision Drivers

* Multi tenant support with own keys for each tenant

## Considered Options

* Asymmetric JWT signing
* Symmetric JWT signing

## Decision Outcome

Chosen option: "Asymmetric JWT signing", because it the only option which allow to use different keys for different tenants.

### Positive Consequences

* multiple keys are supported

### Negative Consequences

* complex management of keys

## Pros and Cons of the Options

### Asymmetric JWT signing

A RSA or ECDSA key pair is used for signing and verification.
The JWTs signed by the external services using their own private key.
Each private/public key pair has a key id and the public key is added as known key to the websocket-api.
The websocket-api uses the key id of the JWT to find the corresponding known public and use it to validate the JWT Token signature.

* Good, because multiple tenants can use the same websocket-api service with different keys
* Good, because adding or revoking of single tenant key is possible
* Bad, because setup of the private and public keys is complicated
* Bad, because multiple keys must be managed

### Symmetric JWT signing

The HMAC algorithm with a shared secret is used for signing and verification.
All the external services must know the shared secret of the websocket-api to generate valid JWTs.
The websocket-api use it secret to validate all JWTs.

* Good, because implementation very simple
* Good, because only a simple secret (string) must be managed
* Bad, because all tenants use the same shared secret
* Bad, because changing the secret require changes to all tenants

## Links

* [ADR-0001](0001-use-json-web-tokens.md)
