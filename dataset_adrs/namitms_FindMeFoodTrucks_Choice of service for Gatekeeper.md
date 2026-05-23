# :bulb: Which service to choose for implementing the Gatekeeper Pattern

:calendar: Date: 2/10/2020

## :heavy_check_mark: Status : Accepted

## :dart: Context

The application APIs have the following requirements around the interfaces

* Should support a rich developer experience
* Should support Gatekeeper pattern for security

The following options for service are considered for this:
* App Gateway
* API Management

Choosing the right service to implement the gatekeeper patter will help optimize the development experience and operational cost

## :traffic_light: Decision

The recommended approach is to use Azure API Management considering the following points:
* Support for a developer portal
* Ability to offload security

## :trophy: Consequences

Azure PI management will enable a developer portal which will help document the APIs better to provide a rich developer experience. 