# 6. Enable host + domain specific one way TLS

Date: 2018-11-13

## Status

Accepted

## Context

Enable one way TLS between front-end and envoy per host+domain that is
specified via gateway config.

## Decision

#### Gateway Configuration

This is achieved by sending the following config from copilot.

```
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: mygateway
spec:
  selector:
    istio: ingressgateway # use istio default ingress gateway
  servers:
  - port:
      number: 443
      name: https-httpbin
      protocol: HTTPS
    tls:
      mode: SIMPLE
      serverCertificate: /etc/istio/ingressgateway-certs/tls.crt
      privateKey: /etc/istio/ingressgateway-certs/tls.key
    hosts:
    - "httpbin.example.com"
  - port:
      number: 443
      name: https-bookinfo
      protocol: HTTPS
    tls:
      mode: SIMPLE
      serverCertificate: /etc/istio/ingressgateway-bookinfo-certs/tls.crt
      privateKey: /etc/istio/ingressgateway-bookinfo-certs/tls.key
    hosts:
    - "bookinfo.com"
```

In the config above each cert and key in the array of servers represent a
host+domain and the path to each cert and the key is arbitrarily chosen.

Copilot extracts the domain information from the cert chains provided in the bosh spec properties:

```
frontend_tls_keypairs:
  example:
    - cert_chain: |
        -----BEGIN CERTIFICATE-----
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        -----END CERTIFICATE-----
      private_key: |
        -----BEGIN RSA PRIVATE KEY-----
        -----END RSA PRIVATE KEY-----
    - cert_chain: |
        -----BEGIN CERTIFICATE-----
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        -----END CERTIFICATE-----
      private_key: |
        -----BEGIN RSA PRIVATE KEY-----
        -----END RSA PRIVATE KEY-----
```

#### Cert Storage

The placement of the certs and keys on the envoy VM is done using a separate
process specific to this purpose. This process will be in charge of knowing
where the certs are located and placing the certs on the correct paths. It is
important for the envoy VM and copilot to agree on a path where the cert and the keys
are stored, and having a specific process to manage this will reduce duplication
and mitigate skew.

## Consequences

* Less skew and duplication
* Certs are not passed around between components in messages, which could
  introduce a security concern
* BOSH may someday introduce a feature that will replace the locator/stower
  process, but this doesn't seem to be in their immediate future
