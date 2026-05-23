# 5. OAuth scope naming conventions

Date: 2021-02-18

## Status

Accepted

## Context

We feel the need to use a naming convention for OAuth scopes.

## Decision

For this coding standard we will follow a [Restful API Guideline](https://opensource.zalando.com/restful-api-guidelines/)
from Zalando.

Guideline [#225](https://opensource.zalando.com/restful-api-guidelines/index.html#225) says that permission names in 
APIs must conform to the following naming pattern:

~~~text
<permission> ::= <standard-permission> |  -- should be sufficient for majority of use cases
                 <resource-permission> |  -- for special security access differentiation use cases
                 <pseudo-permission>      -- used to explicitly indicate that access is not restricted

<standard-permission> ::= <application-id>.<access-mode>
<resource-permission> ::= <application-id>.<resource-name>.<access-mode>
<pseudo-permission>   ::= uid

<application-id>      ::= [a-z][a-z0-9-]*  -- application identifier
<resource-name>       ::= [a-z][a-z0-9-]*  -- free resource identifier
<access-mode>         ::= read | write    -- might be extended in future
~~~

To meet our own naming guidelines, we will use our Solution IDs as the `<application-id>`. The naming convention of 
these Solution IDs are described within our Cloud naming convention page on Confluence.

## Consequences
