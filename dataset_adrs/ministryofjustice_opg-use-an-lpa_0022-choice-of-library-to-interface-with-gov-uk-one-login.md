# 22. Choice of library to interface with Gov.uk One Login

Date: 2023-09-12

## Status

Accepted

## Context

In order to implement the Gov.uk One Login OIDC login service we should ideally select a well-supported opensource
library to provide the main implementation details. The OIDC Authorisation flow is a tricky thing to get right and
needs to be cryptographically secure in its implementation.

Our needs are complicated by the split frontend/api architecture that we have due to the fact that most libraries make
the assumption that they have full control and access of PHP http semantics and tooling (access to cookies, sessions,
raw http header values etc).

The library [`facile-it/php-openid-client`](https://github.com/facile-it/php-openid-client) provides a solid and well tested implementation of the hard parts of the
problem space and a set of optionally usable middleware (that we can adapt or otherwise ignore).

## Decision

We shall use [`facile-it/php-openid-client`](https://github.com/facile-it/php-openid-client) as our OIDC library of choice. Below is a sequence diagram of the roughly
intended flow this library allows.

```mermaid
sequenceDiagram
  participant One Login
  actor User
  autonumber
    User ->>+ service-front: Clicks login button
    service-front ->>+ service-api: Pass users locale
    service-api -->> service-api: Create OIDC redirect url
    Note right of service-api: See \Facile\OpenIDClient\Middleware\AuthRedirectMiddleware<br/>for guidance on usage of<br/>\Facile\OpenIDClient\Service\AuthorisationService
    service-api -->>- service-front: {redirect_uri, AuthSessionInterface}
    service-front -->> service-front: Store AuthSessionInterface in session
    service-front -->>- User: Redirect redirect_uri
    User -->>+ One Login: Follow redirect
    alt Create
        One Login -->> One Login: Account creation
        One Login -->> One Login: Login to account
    else Login
        One Login -->> One Login: Login to account
    end
    One Login -->>- User: Redirect to callback_uri
    User -->>+ service-front: Follow callback_uri
    service-front -->> service-front: Fetch AuthSessionInterface
    service-front -->> service-front: Process query parameters
    break Error
        service-front -->> User: Login failure page (see One Login docs)
    end
    service-front ->>+ service-api: {code, state, AuthSessionInterface}
    service-api -->> service-api: Process OIDC authorisation
    break Error
        service-api -->> service-front: authentication failure exception
        service-front -->> User: Login failure page
    end
    Note right of service-api: See \Facile\OpenIDClient\Middleware\CallbackMiddleware<br/>for guidance on usage of<br/>\Facile\OpenIDClient\Service\AuthorisationService
    service-api -->> service-api: Load User by email from database
    alt User not found
        service-api -->> service-api: Create new user with 'sub'
    end
    alt New One login user or merged previously
        Note right of service-api: User record from DB contains 'sub'
        service-api -->> service-front: UserInterface
        service-front -->> service-front: Store UserInterface in session
        service-front -->> User: Dashboard
    else Merge
        Note right of service-api: User record from DB does not contain 'sub'
        service-api -->>- service-front: {UserInterface, 'sub'}
        service-front -->> service-front: Store unmerged UserInterface in session
        service-front -->>- User: Merge Workflow start
    end
```

## Consequences

We'll be tied to the chosen library and its updates (or lack thereof), though this can be somewhat mitigated with some
sensible usage of interfaces. Additionally the project is MIT licensed so major issues can be solved with a simple fork
of the codebase.
