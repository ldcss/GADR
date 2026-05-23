---
layout: default
title: ADR-0011
nav_order: 14
permalink: records/0011/
---
# Use JSON Web Token ("JWT") for authenticating inter-service API requests

* Status: drafted <!-- required -->
* Decider(s): <!-- required -->
  * SUL DLSS infrastructure developers
* Date(s): <!-- required -->
  * drafted: 2020-04-03
  * ...

## Context and Problem Statement <!-- required -->

SDR is implemented by way of many different discrete services, some of which make network requests of each other to do their work.  For example, at present:

* Argo calls Preservation Catalog to retrieve computed checksums for file content, and to retrieve actual preserved file content.
* Many different services use dor-services-app for read and write operations on our digital repository objects.

Of course, we want to make sure that not just any client on the network can use these services, since access to them should be limited to authorized callers.

In the past, this was accomplished primarily through network access restrictions (e.g., firewall whitelisting IPs of services that should have access, limiting access to clients inside the VPN, etc).  However, sole use of this approach has been deprecated by the industry at large and by Stanford UIT in particular (though it is still an important component of security).

## Decision Drivers <!-- optional -->

* We want to secure access to our API endpoints.
* UIT wants us to secure access to our API endpoints.
* We would like an approach that's relatively easy to understand and maintain.

## Considered Options <!-- required -->

* Gate access to services to which only authenticated clients should be allowed to connect by rejecting client requests which don't inclue a valid auth token.  Specifically:
  * The service to which access should be controlled (e.g. an application serving API endpoints) should be able to mint signed JSON Web Tokens.  The tokens should be generated per the JWT standard, thus each one that's minted will consist of 3 `.` delimited sections:
    * A base64 encoded JSON header with some metadata about the token, including the hash algorithm used for signing (in the `"alg"` field).
    * The token's payload, which will consist of a base64 encoded JSON hash with a `sub` (for "subject") field containing the name of the application for which the token is being minted.
    * A signature generated using a strong HMAC algorithm (e.g. HMAC-SHA256 or HMAC-SHA512 as of this writing) to encode the concatenated (`.` delimited) header and payload (each base64 encoded) using a **securely generated and stored secret of sufficient length**.  Detail provided in the links section about the particulars of secret generation, but in brief, you should probably generate a secret of at least the length of the hash output, e.g. at least 256 bits (32 bytes) for HMAC-SHA256 or at least 512 bits (64 bytes) for HMAC-SHA512.  An easy way to do this is to run `rails secret`, since that will return a random 128 byte hex value.
  * The service to which access should be controlled will look for an `Authorization` HTTP header in all requests for token protected resources.  The header value should be of the form `Bearer <TOKEN>`, where `<TOKEN>` is the token minted for a particular calling service.  A token is validated by decoding it and verifying that the signature portion corresponds to the combination of the token's header/payload and the protected server's signing secret, using the signing hash algo.
  * When a client application needs access to a token protected application, a developer will generate a new token for that client application using the protected application.  See links section below for concrete examples.
    * **WARNING**: Like the signing secret for the token protected service, the generated tokens should be treated as private configuration values, and should not be made public, as this might allow unauthorized clients to pretend to be legitimate callers.
  * _Note_: it's likely that there's a library handy in your language for generating and validating JWTs without having to implement all the above yourself.  E.g. in Ruby, the `jwt` Gem provides a `JWT.encode` method that takes the payload (as a hash), the secret value (as a string), and the name of the hash algorithm to use (as a string).  it has a `.decode` counterpart method for token reading and validation.
  * If a specific client token is compromised, there are two options for revoking it:
    * Rotate the server's signing secret.  This will effectively invalidate all client tokens and require new tokens to be minted using the new signing secret.  If the security situation is urgent, this is probably the safest and most expedient approach.
    * Implement blacklist functionality in the protected application that can reject specific tokens, e.g. either by payload contents or token value.  If this route is taken, make sure that the implementation is well tested (and please add a link to it at the bottom of this doc!).
  * If a server's signing secret is compromised, the signing secret _must_ be rotated, and all client tokens _must_ be re-generated with the new secret.
  * The basic JWT approach we're using does not lead to automatic token expiry, though the standard doesn't preclude token expiry.
  * Note that some API routes in some applications may need to be opted out of token protection.  E.g. a Resque or Sidekiq dashboard meant for human access should instead be protected by Shib/webauth, not JWTs.  See preservation_catalog validation link at end for an example implementation of this.

We have not seriously discussed other options.  Another approach which also uses cryptography to prove client identity would be authentication via client certificates.  Fedora 3 (our current digital repository backend) uses this approach.  If we were to do this, each client application would generate its own public/private key pair, and the public key would be registered with the server to which access is desired. Thus, the client with its private key could prove its identity by decrypting for the protected service a challenge the protected service encrypted using the client's public key.  In DLSS' ecosystem, it's likely easier to implement a JWT based approach (we have a very concise pattern for Ruby/Rails), and the JWT based approach should be completely adequate for proving caller identity (assuming the above guidelines re: secret selection/storage and hash algo choice are followed).

## Decision Outcome <!-- required -->

The infrastructure team came to consensus in a weekly planning meeting that, going forward, we should gate access to API endpoints using JWTs (minted by the service, provided with requests by the client).  This ADR is meant to capture and flesh out that decision.

### Positive Consequences <!-- optional -->

* More robust and less circumventable than restricting access solely by way of network and firewall configuration.
  * Does not preclude keeping appropriate firewall restrictions, which should remain part of our security practice.
* Should a network re-configuration result in accidental loosening of firewall restrictions, token based authentication provides a robust additional line of access control.
* For the ways we've built our applications, token based authentication is at least as easy to implement and maintain as client certificate based authenication, and should provide similarly adequate security.
* Minting tokens has become a common approach in industry for authenticating client access to APIs, so there is a wealth of current information and advice available online for this practice.

### Negative Consequences <!-- optional -->

* More work for developers than solely relying on firewall rules and network configuration (tasks which typically fall to operations and which should happen anyway).

## Links <!-- optional -->

* [Glossy collection of JWT introductory resources](https://jwt.io/)
* [JWT RFC](https://tools.ietf.org/html/rfc7519)
* Concise [Wikipedia entry](https://en.wikipedia.org/wiki/JSON_Web_Token) explaining structure, use, implementing libraries, and possible shortcomings of JWT-based auth
* Choosing secrets for use with HMAC algorithms:
  * [Useful post](https://security.stackexchange.com/questions/95972/what-are-requirements-for-hmac-secret-key/95977#95977) in useful Stack Exchange thread ([archive.org link](https://web.archive.org/web/20150910174628/http://security.stackexchange.com/questions/95972/what-are-requirements-for-hmac-secret-key/95977#95977))
  * [The section of the HMAC RFC](https://tools.ietf.org/html/rfc2104#section-3) that provides the meat of the most concise and useful answer in that thread
* Example implementation in dor-services-app (current as of 2020-04-03)
  * [documentation](https://github.com/sul-dlss/dor-services-app#authentication)
  * [token minting code](https://github.com/sul-dlss/dor-services-app/blob/c473e7528858dfef0a58514e75e9b287b7963010/lib/tasks/jwt.rake)
  * [token validation code](https://github.com/sul-dlss/dor-services-app/blob/c473e7528858dfef0a58514e75e9b287b7963010/app/controllers/application_controller.rb#L23-L32)
* Example implementation in preservation_catalog (current as of 2020-04-03)
  * [documentation](https://github.com/sul-dlss/preservation_catalog#authn)
  * [token minting code](https://github.com/sul-dlss/preservation_catalog/blob/5e9a1b626ca6029f3bd7f61f78756b75fd8c6a28/lib/tasks/jwt.rake)
  * [token validation code](https://github.com/sul-dlss/preservation_catalog/blob/5e9a1b626ca6029f3bd7f61f78756b75fd8c6a28/app/controllers/application_controller.rb#L23-L36)
  * [coordinating GitHub ticket](https://github.com/sul-dlss/preservation_catalog/issues/1298)
* For comparison:  [overview](https://github.com/LD4P/sinopia_server/wiki/Authentication-and-Authorization-in-Trellis) of a somewhat different JWT based authentication/authorization approach, using a 3rd party identity provider (Amazon Cognito) to issue JWTs that do expire (and which are signed/validated using the identity provider's private/public keys).  These tokens are issued to human users (behind the scenes in their browser) upon successful username/password login in Sinopia Editor.  Note this approach illustrates how JWTs can facilitate more granular authorization than what's described above.
