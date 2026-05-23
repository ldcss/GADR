# 1. Migrate to PiHole

Date: 2020-08-07

## Status

Status: Accepted on 2020-08-07  

## Context

Blocking ads at the DNS level would save bandwidth and provide a better user exprience on the home network. To provide that functionality, I would like to use PiHole.

## Decision

Replace stock dnsmasq with PiHole docker image.

## Consequences

* Less ads on the network
* Some systems that require ads may not work, depending on the denylists used.

## Learnings

### Stubby

The arm image of stubby that I am using is based on a good one that actually locks the stubby process into userland. As such, it cannot bind to port 53. This is annoying, but makes sense from a security/best-practices perspective. The default of 5353 is usable through the `ip#port` pattern that DNSMasq (and, hence, PiHole) support. 

The stubby config is not supported through environment variables. Mapping a config file is the only way to fix this. The default config can be exported by running cat in the container.

### PiHole

PiHole is a beast of a docker container. It doesn't seem to align with docker best practices and even the config directories are overwritten on each load as it attempts to upgrade all blacklists on load. 

The health check is not accurate - The container reports as online even when the web page is not available.
