# 3. Store configuration into local storage

Date: 2019-03-29

## Status

Accepted

## Context

To provide the required functionality for the pilot we need to store some
configuration in a persistent way while just operating within a browser
environment. This state could be written to a backend database, or we could
just store into localstorage.

## Decision

We will store the user's configuration into localstorage protected by a PIN
code.

### Proposed storage structure

```json
{
  "1234": {
    "keypair": {},
    "blindSignature": {},
    "devices": {
      "abc123": {
        "longitude": 12.2,
        "latitude": 52.4,
        "exposure": "INDOOR",
        "communities": {
          "2a745dac-015a-4cde-a348-75bccc21502b": {
            "authorizable_attribute_id": "6a1ba9b1-3f20-4e12-ae65-154c5eb7e00f",
            "credential": {},
            "blindproofCredential": {}
          }
        }
      }
    }
  }
}
```

Please see `./localstorage.json` for a complete example including zenroom credentials.

## Consequences

Data stored in localstorage is not in any way secure, so this implementation
is only suitable for this stop gap application.
