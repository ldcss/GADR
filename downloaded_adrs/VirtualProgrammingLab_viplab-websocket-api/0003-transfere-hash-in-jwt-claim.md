# Transfer hash in JWT Claim

* Status: proposed
* Deciders: Leon Kiefer
* Date: 2019-11-07

## Context and Problem Statement

We have to transfer json data and verify the integrity of the json data model.
[ADR-0002](0002-use-sha256-with-base64url-encoding.md) describes how to create a hash of the json.
The hash must be transferred to from the authorization server to the WebSocket API secure.
The validity of the hash must be verified.

## Decision Drivers <!-- optional -->

* JWT should be used

## Considered Options

* Transfer hash in JWT Claim

## Decision Outcome

Chosen option: "Transfer hash in JWT Claim", because it's the only option when using JWT.

### Positive Consequences <!-- optional -->

* multiple hashes for different json documents can be added in one JWT

## Pros and Cons of the Options <!-- optional -->

### Transfer hash in JWT Claim

The JWT Claim used to authorize the user to the WebSocket API contains the claims for the json data that should be used.
The Claims are key-value pairs were the key should be namespaced and describe the json data type and the value is the hash of the concrete json data.
The json data are not included in the JWT only the hash as described by [ADR-0002](0002-use-sha256-with-base64url-encoding.md).

* Good, because small JWTs
* Good, because all authorization data in one place
* Bad, because all json data must be know when creating the JWT

## Links <!-- optional -->

* [ADR-0001](0001-use-json-web-tokens.md)
* [ADR-0002](0002-use-sha256-with-base64url-encoding.md)
