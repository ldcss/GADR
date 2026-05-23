# 4. Cookie Encryption

Date: 16/03/2017

## Status

Superceded by [5. Add Synthetic max-age to Session Cookie](0005-add-synthetic-max-age-to-session-cookie.md)

## Context

### Protect Personal Data at Rest
If a users' device gets compromised then the attacker will not be able to see
the values they've submitted to us.

### Prevent Session Tampering
We don't want to open an attack vector where people can fuzz values that go
into our system so we would either need to sign or encrypt our cookies.

### Data in Transit
This will not make data in transit any safer as it's already encrypted at the
transport level.

### Encryption (and MAC) Algorithm 

### AES-256

The NSA have [declared](http://csrc.nist.gov/groups/ST/toolkit/documents/aes/CNSS15FS.pdf) AES-256 safe enough for top secret data.

AES is a low ram and high speed algorithm which is important when trying to keep
page load times down.

#### Salt
A salt is used to ensure that two items with the same value don't, when
encrypted equal the same output value. We're using a buffer of 256 bits salt the
encrypted cookie.

### Iron Library
At a high level the seal process follows these general steps:

* generate encryption salt `saltE`
* derive an encryption key `keyE` using `saltE` and a password
* generate an integrity salt `saltI`
* derive an integrity (HMAC) key `keyI` using `saltI` and the password
* generate a random initialization vector `iv`
* encrypt the serialized object string using `keyE` and `iv`
* mac the encrypted object along with `saltE` and `iv`
* concatenate `saltE`, `saltI`, `iv`, and the encrypted object into a URI-friendly string

You can read more about it in the Iron 
repository: https://github.com/hueniverse/iron

## Decision

### We will encrypt cookies using the [Iron] library with AES-256
salted with 256 bits.

## Consequences

The payload we send in the cookie will always round up to the next block size
so we're always wasting some bandwidth. 

The salting & encrypting will mean that the the payload will not compress well.

By sending over HTTPS we're encrypting the same data twice without getting any
benefit.

Because the payload is encrypted it's likely that developers will forget
log statements in the code when trying to debug the contents of the cookie
instead of just looking at an un-encrypted cookie in their browser's developer
tools. 

[Iron]: https://github.com/hueniverse/iron
