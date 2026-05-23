# 4. SendLoginFromBackend

Date: 2019-04-15

## Status

Accepted

## Context

For the app to be able to login a user to the dashboard it needs to send a
blind proof credential for the correct authorizable attribute/community to
the dashboard.

The login flow starts by the user being given a URL with the following two
parameters: `sessionId` and `callback`. The `sessionId` value must be passed
back to the dashboard so the correct user can be identified and a session
created, and the `callback` url is where the request must be sent.

The page rendered by the webapp must show a content like saying:

> BCNNow requires a credential to log you in.

> You can login by sharing a secure credential with the dashboard.

> [Login Button]

On pressing the Login button the front end needs to start the process to log
the user in described below.

On successfully logging in the app should send a login request to the
dashboard somehow (structure described below), and display a successful login
message.

## Decision

The Vue front end will send the required information to the backend via the
existing websocket/channels; the backend will receive the message from the
front end, and then wrap it up and send it on to the dashboard api over HTTP.

### Front end message

The message will be emitted as a `dashboard-login` event with the following body:

```json
{
  "callback": "http://bcnnow.decodeproject.eu/oauth/iot_login_callback",
  "request": {
    "sessionId": "abc123",
    "credential": {
      "authorizable_attribute_id": "foobar",
      "value": {
        "proof": blind_proof_credential.proof
      },
      "credential_issuer_endpoint_address": "https://credentials.decodeproject.eu"
    },
    "optionalAttributes: []
  }
}
```

The backend will receive the above message, and attempt to send the request
to the given callback URL. This could have just been done directly by the
front end here, but we will treat like all other requests, i.e. the front end
only sends socket messages to the backend, and the backend is responsible for
sending out all remote requests.

So the backend will send the request object to the specified callback URL
which will either return 200 OK or an error. This value must be returned to
the frontend via a reply to the channel (either `ok` or `error`).

On receiving the response in the front end we will either render a success or
failure message.

## Consequences

By funnelling the message through the backend we don't introduce any new
behaviour to the front end to send HTTP requests. The latency of such a
process might be slightly higher, but only by milliseconds, so I don't
anticipate any great difficulty.
