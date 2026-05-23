# 39. Least privilege access

Date: 2020-09-21

## Status

Accepted

Implements [6. Implement Security by Design](0006-implement-security-by-design.md)

Implemented by [40. HPA](0040-hpa.md)

Implemented by [58. API is trust boundary ODH](0058-api-is-trust-boundary-odh.md)

## Context

The principle of least privilege means that every module (such as a process, a user, or a program, depending on the subject) must be able to access only the information and resources that are necessary for its legitimate purpose.
The principle of least privilege works by allowing only enough access to perform the required job. In an IT environment, adhering to the principle of least privilege reduces the risk of attackers gaining access to critical systems or sensitive data by compromising a low-level user account, device, or application. Implementing the principle helps contain compromises to their area of origin, stopping them from spreading to the system at large.

## Decision

We will apply the principle of least privilege.

## Consequences

### Advantages

* Contains compromises to the area of origin, reducing impact of attacks.
* Reduced risk of leaking confidential information as only parties needing it have access.

### Disadvantages

* Additional identity and access management at different layers introduces overhead and additional cost.

## References

* https://en.wikipedia.org/wiki/Principle_of_least_privilege, retrieved 29 October 2020
* https://digitalguardian.com/blog/what-principle-least-privilege-polp-best-practice-information-security-and-compliance, retrieved 29 October 2020
