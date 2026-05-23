# Use JSON Web Tokens

* Status: accepted
* Deciders: Leon Kiefer, Per Pascal Seeland, Anett Seeland
* Date: 2019-11-07

## Context and Problem Statement

External services must authorize web clients to the WebSocket API.
The WebSocket API is stateless and not maintain a user Session with Cookies.
Only little data should be stored for an open WebSocket connection.

## Decision Drivers

* decoupling of the authorization service and the WebSocket API
* flexible and well supported on many platforms

## Considered Options

* JWT from pre-shared keys
* Basic Auth
* OAuth 2.0

## Decision Outcome

Chosen option: "JWT from pre-shared keys", because the WebSocket API is loosely coupled and it is well supported on many platforms.

### Positive Consequences

* Simple to implement
* Authorization data can be send in a portable and verifiable way

### Negative Consequences

* The shared keys must be handled

## Pros and Cons of the Options

### JWT from pre-shared keys

External service and WebSocket API have a pre-shared key (this does not mean it's a symmetric key).
Each external service has it's own pre-shared key to identify it.
The external services uses the pre-shared key to generate JWTs and add authorization data in the JWT Claims to allow clients access to parts of the WebSocket API.

* Good, because it is simple to implement
* Good, because many libraries available for almost all platforms
* Good, because authorization data can be included in the JWT
* Bad, because the pre-shared keys must be handled by the services

### Basic Auth

The client uses credentials like username and password to authenticate to the WebSocket API.
The WebSocket API manages the access control for clients and the external service can give clients the access.

* Good, because authorization is done only on the server side
* Bad, because user management must be implemented in the WebSocket API
* Bad, because access control must be implemented in the WebSocket API
* Bad, because each client need own credentials

### OAuth 2.0

Similar to [Basic Auth](#basic-auth) but the authorization is done using OAuth 2.0.

* Good, because integration of OAuth 2.0 Service
* Bad, because an OAuth 2.0 is required and must be configured for the correct access control
* Bad, because user management must be implemented in OAuth 2.0 Service
