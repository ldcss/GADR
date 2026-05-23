# Simplified Architecture

## Status

Proposed

## Context

In the following diagram contrast the current architecture (top diagram) versus the proposed architecture (bottom diagram):

![fulfilment-lambdas-architecture](https://user-images.githubusercontent.com/13835317/72334391-25d64000-36b5-11ea-95be-47bc51eb648f.jpg)

**Problems with current architecture**

* Many moving parts - five different Lambdas + Step Function + API Gateway + S3
* Different implementations for Guardian Weekly and Home Delivery
  * for example, GW is automatically uploaded, and does not use an API, whilst HD is manually uploaded via API
* Uses streaming even though total file size seems to be <20MB
* server-side heavy project written in JavaScript + Flow which is non-standard for SX, because SX mostly uses Scala for server-side, and JavaScript + TypeScript client-side

## Decision

TODO

## Consequences

**Arguments for**

* Less moving parts
    * single lambda, no need for streaming, no need for S3, direct upload to Salesforce, no need for API, no need for Step Function
    * file generation is completing within 15 minutes so single lambda is viable
* Alerting and fallback mechanisms would still be in place
* Rewriting it in Scala would fit with the rest of [`support-service-lambdas`](https://github.com/guardian/support-service-lambdas)
* This is a critical path for SX, and we could re-design around alarming from the get-go.
* Maintenance cost will likely be lower than now. For example, the current issues encountered due to Node upgrade, would likely not happen on Scala codebase, or at least might have been quicker to resolve.
* We could integrate `fulfilment-date-calculator` by design instead of retrofitting

**Arguments against**

* Critical path with complicated current implementation, which means we would have to be very careful to replicate the very same behaviour in a different codebase
* Non-trivial task from both implementation and QA perspective, which is likely to take couple of sprints. If implementation is successful, we would need a period of time to run both codebases simultaneously to make sure behaviour is exactly the same, before switch-over.
What becomes easier or more difficult to do because of this change?

