More info:
http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions

# Short title
How will we ensure our API access is secure?

# Status
CLOSED

# Context
We're creating a replacement for the Dynamics 365 interface to our data, which does not include sensitive data but does include personally identifiable information.
The Dynamics API requires authentication with a set of credentials configured within the relevant Dynamics environment.

The API _must_ not be open to public use (must not provide data without authentication)
The API is hosted on our Azure infrastructure, but is assumed to be publicly discoverable

# Options
- Use a service provide a means to authenticate the request such as Azure API Management & Active Directory
- Manually provision and check user identities
- Block all traffic to the API and use an IP whitelist

There are further considerations depending on the option chosen.

# Decision
- Manually provision a way for users to authenticate requests using the simplest means possible that provides necessary security.

# Rationale
We've chosen to create a simple API key system where each request to the API is required to provide a valid API key or the request is rejected.

We will manually provision and check these keys

We will load our provisioned keys from config on start up as a lookup - [User, key]

Each request will be checked for the presence of of a header key/value pair with the key `X-API-Key`, and the provided value must be a valid configured key or the request will be rejected with the FORBIDDEN status code.

We believe using an API gateway or having consumers authenticate via Azure Active Directory/API Management and present a token are valid options but require more development investment, where a simple set of provisioned keys can be secure, performant and _importantly_ controlled by the team that owns the API.

Because we have designed our API key check to check against an in-memory lookup, the following apply:
 - Key checks can be made performantly for every request
 - We can provision or delete keys in seconds, via configuration
 - Changes in configuration (at this time) require redeployment to take effect, but we can offer seamless deployment
 - Configuration values are _never_ committed to source code, so we can continue to work in the open
 - Testing (UI and integration) is easily done in an automated way using test configurations, and we can provision unique keys for test environments

This approach was also implemented very quickly and before any other API functionality was implemented. Its low resistance as an approach allowed us to deploy working test environments rapidly with confidence that _no_ deployment would ever expose data unsecured.

In future, we will consider migrating to a provided service or integrate with the existing Active Directory system in order to allow more fine-grain control of permissions, and to allow support of larger numbers of unique consumers. This approach will work for our expected scale, but could become difficult to maintain at larger than expected numbers. To do so now, compared to the very low overhead of implementing the actual header key check would be a significant investment for a small gain.

# Dependencies
Confirmation this does not affect the authority to operate.

Teams need to know how to make configuration changes to provision or delete keys.

Users are required to request access to the API environments and await key provisioning, keys need to be generated, shared and configured in a secure way.

# Impact
Users will have a lead up time to integration and cannot self-service generate keys, conversely key/account provisioning is not reliant on Active Directory Administration and the lead up time is expected to be less than one day.

This approach is as secure as the keys are treated - we will need to establish an appropriate process and communication channel (via Live Service Support) to report accidental compromise of keys. Keys can be revoked and replaced in a matter of minutes.

# Contributors

- Christopher Gunn
- Steve Leighton
- Lewis Dale
- Daniel Burnley
- Vivian Roberts

# Supporting Info (optional)

N/A
