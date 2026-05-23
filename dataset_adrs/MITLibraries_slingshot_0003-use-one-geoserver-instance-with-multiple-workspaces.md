# 3. Use One GeoServer Instance With Multiple Workspaces

Date: 2019-07-01

## Status

Accepted

## Context

There are a few problems that need to be solved around handling authentication with GeoServer:

1. We have some layers which can only be accessed by authenticated users and some that are publicly accessible.
2. The user never interacts directly with GeoServer. Requests to GeoServer for data come from the user's browser either through `img` tags or through AJAX requests from Leaflet. This means the user needs to be preauthenticated with GeoServer in some way.
3. GeoServer's authentication is incredibly difficult to work with.

In the past, we solved these problems by leveraging the SSO capabilities of Shibboleth and simply running two GeoServer instances--one that was publicly accessible and one that was behind Shibboleth. Touchstone authentication happened for the user through the Rails application. Given the decision to move away from Shibboleth this is no longer an option. Running two GeoServer instances also adds additional burdens to deployment, management and the data publication process.

## Decision

Run a single GeoServer instance. GeoServer supports what it calls workspaces, which is just a way of partitioning layers within the system. The authentication for each workspace can be configured separately. Configure one workspace to be readable by anyone and one workspace to require Basic Auth using a predefined username and password.

Access to this GeoServer instance will need to be proxied. The proxy (our Geoblacklight instance) will handle SAML authentication and augment the proxy request to GeoServer with the Basic Auth login if the user has authenticated with Geoblacklight.

## Consequences

The biggest consequence of this approach is that Rails will now need to function as a proxy in addition to its job of running Geoblacklight. Our instance sees relatively low usage so I would consider the risk of any sort of DoS under normal usage pretty small. The proxying can happen early in the Rails process as it only needs to know if the user is authenticated. In other words, the proxy can be inserted in the Rack middleware right after Warden, thus bypassing most of Rails.

If this does become a performance problem, there's unfortunately no easy way to mitigate it. Geoblacklight can't quite be scaled horizontally, though I believe with a little work it could be made to support it. This would probably be the easiest solution if it were needed.
