# 4. Create software defined everything

Date: 2020-09-21

## Status

Accepted

Implemented by [42. Python version 3](0042-python-version-3.md)

Implemented by [43. API First](0043-api-first.md)

Implemented by [44. OpenAPI3](0044-openapi3.md)

Implemented by [45. Code / config separation](0045-code-config-separation.md)

Implemented by [46. Javascript framework](0046-javascript-framework.md)

Implemented by [47. Shell scripting](0047-shell-scripting.md)

Implemented by [48. Testing framework](0048-testing-framework.md)

Implemented by [49. gitops Deployment](0049-gitops-deployment.md)

Implemented by [50. Expand pip requirements](0050-expand-pip-requirements.md)

Implemented by [51. Declarative preferred over actions](0051-declarative-preferred-over-actions.md)

Implemented by [52. ODRL policy](0052-odrl-policy.md)

Implemented by [53. Project company data](0053-project-company-data.md)

Implemented by [54. Coding guidelines](0054-coding-guidelines.md)

Implemented by [55. Feature toggles over feature branching](0055-feature-toggles-over-feature-branching.md)

Implemented by [12. Data catalog specifies all data components](0012-data-catalog-specifies-all-data-components.md)

Implemented by [13. Data retention defined on each data component](0013-data-retention-defined-on-each-data-component.md)

Implemented by [41. Deployment through Pull Request](0041-deployment-through-pull-request.md)

## Context

Software-defined everything (SDx) is the definition of technical computing infrastructure entirely under the control of software with no operator or human intervention. It operates independent of any hardware-specific dependencies and is programmatically extensible.

In the SDx approach, an application's infrastructure requirements are defined declaratively (both functional and non-functional requirements) such that sufficient and appropriate hardware can be automatically derived and provisioned to deliver those requirements.

The benefits of SDx is that it lowers/eliminates effort towards infrastructure maintenance, allows companies to move focus to other parts of the software, ensures consistence while also allowing for extensibility, remote deployment through configuration without downtime, and allows you to leverage the power of versioning such as git.

## Decision

Where possible software and infrastructure (or whatever) are deployed from source code. No human management of software and infrastructure is performed.

## Consequences

### Advantages
Advanced capabilities enable the transition from one configuration to another without downtime as mentioned before, by automatically calculating the set of state changes between one configuration and another and an automated transition step between each step, thus achieving the complete change via software.

### Disadvantages
Developing an SDx-ready organization requires people who have the right mindset, not just the right skill set.

