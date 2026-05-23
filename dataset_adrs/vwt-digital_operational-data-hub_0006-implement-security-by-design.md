# 6. Implement Security by Design

Date: 2020-09-21

## Status

Accepted

Implemented by [30. life cycle management](0030-life-cycle-management.md)

Implemented by [31. Uniform bucket-level access for storage](0031-uniform-bucket-level-access-for-storage.md)

Implemented by [32. Oauth2 for authentication](0032-oauth2-for-authentication.md)

Implemented by [33. Two identity providers: development / run](0033-two-identity-providers-development-run.md)

Implemented by [34. 2FA on all user identities](0034-2fa-on-all-user-identities.md)

Implemented by [35. All communication uses SSL](0035-all-communication-uses-ssl.md)

Implemented by [36. SSL certificates are always verified](0036-ssl-certificates-are-always-verified.md)

Implemented by [37. Secrets are stored in GCP Secret Manager](0037-secrets-are-stored-in-gcp-secret-manager.md)

Implemented by [38. SAST and DAST are in the CI/CD pipeline](0038-sast-and-dast-are-in-the-ci-cd-pipeline.md)

Implemented by [39. Least privilege access](0039-least-privilege-access.md)

Implemented by [40. HPA](0040-hpa.md)

Implemented by [41. Deployment through Pull Request](0041-deployment-through-pull-request.md)

Implemented by [58. API is trust boundary ODH](0058-api-is-trust-boundary-odh.md)

Implements [59. Runtime dependency only on GCP](0059-runtime-dependency-only-on-gcp.md)

## Context

Secure by design, in software engineering, means that the software has been designed from the foundation to be secure. Secure by Design is more increasingly becoming the mainstream development approach to ensure security and privacy of software systems. In this approach, security is built in the system from the ground up and starts with a robust architecture design.
“The problem is: 95 percent of successful attacks are due to poorly programmed, poorly maintained or poorly configured software,” says Thomas Tschersich, Head of Internal Security & Cyber Defense at Deutsche Telekom.

## Decision

Security is built-in in all our designs from the start. Security is not something which is built in afterwards.

## Consequences

* All security related issues need to be handeled with high prioroty.
* Security awareness should be on everyones mind
* Security related issues should be trained regular

