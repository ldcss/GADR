# Use SHA256 and Base64Url encoding for verifying json

* Status: proposed
* Deciders: Leon Kiefer
* Date: 2019-12-13

## Context and Problem Statement

We have to transfer json data and verify the integrity of the data.
The transfer involves an Authorization server which provides the json, a client which gets the data form that server and pass it to the WebSocket API.
The WebSocket API must able to verify the integrity of the json data.

## Decision Drivers <!-- optional -->

* Use standard encodings

## Considered Options

* Transfer complete json via secure channel
* Send SHA256 hash of Base64Url encoded json
* Send SHA256 hash of formatted json

## Decision Outcome

Chosen option: "Send SHA256 hash of Base64Url encoded json", because this method is platform independent and not much session state is required.

### Positive Consequences <!-- optional -->

* The JWT really function as a verification token for the other requests.
* Can be applied to all json data that must be verified.

### Negative Consequences <!-- optional -->

* The json must be transferred in Base64Url encoding

## Pros and Cons of the Options <!-- optional -->

### Transfer complete json via secure channel

The complete json data is transferred using a secure channel, like a JWT Token Claim.
The secure channel takes care of the Integrity and the transport.

* Good, because well known solutions can be used.
* Good, because very secure.
* Bad, because depending on selected secure channel many data have to be stored in a session state.
* Bad, because there are limitations how many data can be transferred at once using a secure channel.

### Send SHA256 hash of Base64Url encoded json

The json is encoded with Base64Url encoding (RFC 4648).
The Base64 String is then transferred instead of the raw json.
For the Base64 string the message digest using SHA256 (FIPS PUB 180-4) is computed and used to verify the integrity.
The message digest is a sequence of bytes and should be encoded to a lower-case hex string to transfer it over a secure channel like JWT.

* Good, because the Integrity of the json can be verified simply.
* Good, because only the small hex encoded message digest must be transferred over a secure channel.
* Bad, because the json is transferred Base64 encoded and must be decoded before use.
* Bad, because this must be implemented by hand.

### Send SHA256 hash of formatted json

The json can be transferred in any format.
To verify the integrity, the json is formatted in a way, that the same json info set result in the same json string representation on all platforms.
This json string is then hashed using SHA256 (FIPS PUB 180-4) and the message digest can be used the verify the integrity.
The message digest is a sequence of bytes and can be Base64Url encoded to transferred it over a secure channel like JWT.

* Good, because only the small Base64 encoded message digest must be transferred over a secure channel.
* Good, because json can be be transferred as is.
* Bad, because difficult to get a consistent formatting across platforms.
* Bad, because heavily depends on the json formatting library
* Bad, because this must be implemented by hand.

## Links <!-- optional -->

* [ADR-0001](0001-use-json-web-tokens.md)
* [ADR-0003](0003-transfere-hash-in-jwt-claim.md)
