# Definition of 'environment'

## Status

Proposed

## Context

The term 'environment' is incredibly overloaded and means different things to different people
even on the same team. In the context of CNP infrastructure and applications, one developer's environment might be
another's Azure subscription, or might be another's demo application location.

In the Jenkins library code, the single variable `environment` (or `env`, etc) is passed around with different meanings at both the calling and receiving sites. This causes confusion and makes understanding and debugging the library difficult. Also, having 3 separate concepts represented by a single variable introduces a source of potential bugs and reduces the flexibility of the overall solution. E.g. at the moment we can only have one environment per subscription.

Where developers have realised this limitation, other terms and variable names have been used locally but there is no consistent, shared set of terms so different names have been used to represent the same concepts.

## Decision

Use three terms consistently to distinguish between the subscription, environment and application context.

The three terms are:

| Term | Variable name | Example values | Definition |
| ---- | ----|  ----------- | -- |
| Subscription | `subscription`| `nonprod`, `prod` | The identifier of the Azure subscription to use for infrastructure operations. |
| Environment | `environment` | `dev`, `aat`, `prod` | A named instance of an Azure ASE and all the supporting infrastructure including DNS, WAF, etc. Three instances named `dev`, `aat` and `prod` will exist by default. The special value `prod` will always represent environments in the `prod` subscription, all other environments will exist in the `nonprod` subscription. |
| Application Context (TBA) | `application_context` | `demo1`, `aat`, `prod` | An application-level suffix to support deploying the same application many times in the same environment. In particular, allowing for named demo and exploratory instances of the application to deploy to the `dev` environment. The value could, for example, be the (non-`master`) branch name. The special values `aat` and `prod` are only deployable from the `master` branch and map to the `aat` and `prod` environments respectively. |

These terms should have a consistent meaning across all method and function calls. Method
and function definitions should use the convention above.

## Consequences

* Check all method definitions to make sure the correct variable name is used.
* Refactor code to use multiple, different, correctly-named variables where more than one concept is being described. This may mean that method signatures need to be modified to take additional parameters.
* Application infrastructure code will need to specify 3 variables instead of one (currently it just has `env`) to correctly identify existing state storage locations and to correctly name new infrastructure components. E.g. it will need to use the `subscription` and `environment` values to locate the remote state storage for the core-compute to deploy the app to and will need the `application_context` value to create the correct name for the application in the ASE.
* Application pipeline will need to pass the 3 values to the infrastructure code when it is being built. The rules above relating to special values for `environment` and `application_context` can be used.
