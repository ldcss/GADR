# 34. 2FA on all user identities

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

## Context

Two-Factor Authentication (2FA) is sometimes called multiple factor authentication. In simple terms, it adds an extra layer of security to every online platform you access. The first layer is generally a combination of a username and password. Adding one more step of authenticating your identity makes it harder for an attacker to access your data. This drastically reduces the chances of fraud, data loss, or identity theft.

Passwords have been the mainstream form of authentication since the start of the digital revolution. But, this security measure is far from infallible. Here are some worrying facts about this traditional security measure:
* 90% of passwords can be cracked in less than six hours.
* Two-thirds of people use the same password everywhere.
* Sophisticated cyber attackers have the power to test billions of passwords every second.

The vulnerability of passwords is the main reason for requiring and using 2FA.

## Decision

We will use 2FA on all user identities.

## Consequences

Despite the additional overhead of the second factor to authenticate, the additional protection of the user identity is worth the effort. Most identity providers facilitate 2FA using a mobile app, which limits the additional effort required.

## References

* https://secureswissdata.com/two-factor-authentication-importance/, retrieved 21 October 2020
