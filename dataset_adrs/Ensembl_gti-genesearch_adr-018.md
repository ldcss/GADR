# ADR 018: Profile-based search implementations

## TL;DR
The application needs to be run using either htsget EBISC or Ensembl ES variations. This is now triggered using Spring profiles.

## Context
We need to be able to run the application using different search backends in different scenarios. Rather than using a complicated if-else switch in EndpointSearchProvider, there are now multiple instances that extend from a common EndpointSearchProvider class. 
These are 
* EnsemblVariationEndpointProvider - profile `default`
* EnsemblRESTVariationEndpointProvider - profile `ensembl_rest`
* EVAMongoEndpointProvider - profile `eva_mongo`
* EVAEndpointProvider - profile `eva_rest`
* EbiscEndpointProvider - profile `ebisc`

Profiles are set at runtime via the property `spring.profiles.active`. If not set, the default profile will be used. This allows rapid switching of implementations at startup.

## Status
Testing

## Consequences
Profile needs to be set if non-default profile required.
Tests need to have profile set e.g.
```
@WebIntegrationTest({"spring.profiles.active=eva_mongo"})
@ActiveProfiles("eva_mongo")
```

## Tags
