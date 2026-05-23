# 3. Add GOV.UK Frontend

Date: 21 December 2018

## Status

Accepted

## Context

The existing site was built using [GOV.UK Elements](https://govuk-elements.herokuapp.com) which comprised of 3 separate npm packages, which have been copied into the project as one-offs.

Elements has since been deprecated, in favour of the [GOV.UK Design System](https://design-system.service.gov.uk), which is being actively maintained.

## Decision

We should include the [govuk-frontend](https://github.com/alphagov/govuk-frontend) repository using the NPM package manager, and then compile all of the relevant SASS files into our main application CSS file. This allows us to then slowly start using the Design System, as the class names have been designed not to conflict with the ones from Elements.

Pros
----
* We are able to benefit from the ongoing features and improvements developed by the Design System team.

Cons
----
* In the short term, this makes our CSS file bigger, and take longer to download, as it includes _both_ the Elements CSS and the Design System CSS. Once we have fully switched, we will be able to remove the Elements CSS.

## Alternatives

We could try to move across to the Design System styles all in one go, rather than gradually. This would mean a smaller CSS file, but would be more up front work, and more risk.

## Consequences

Developers will have to acquaint themselves with the Design System, and we should also start namespacing our own CSS components.
