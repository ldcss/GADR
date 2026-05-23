---
id: adr-0002-api-documentation
title: 2 - API Documentation
---

# Context

Granary will be a standalone deployable open source application. Users' primary
way of interacting with Granary will be through its REST API, rather than
through a UI, at least for the foreseeable future. This focus puts a larger
burden than usual on the quality of our API documentation.

We'd like to evaluate different ways to keep API documentation up-to-date. For
each strategy, we want to know:

- What are the general pros and cons?
- How do we find out that our docs have drifted from the API?
- How can we document different versions of the API at the same time?

## The contenders

I evaluated three software solutions that rely on code/documentation generation
and also a process solution. The three libraries I considered were
[`rho`](https://github.com/http4s/rho),
[`tapir`](https://github.com/softwaremill/tapir), and
[`guardrail`](https://github.com/twilio/guardrail). For the software solutions,
I created a small repository [here](https://github.com/jisantuc/scala-api-doc/).

## Manual API spec maintenance

The most successful way we've done this in the past was a spec-first
development pattern. In this pattern, we added endpoints to the API spec, then
implemented them only after the spec changes were merged. We drifted away from
this over time, and eventually wound up with a checklist item in our pull
request template that specified that the API spec had been updated. For a long
time, our spec wasn't valid Swagger, which we found out about when we tried to
create a docs site. For a while after that, parts of our spec were
incorrect, which we found out about when users attempted to use the spec for
API interaction (though there were other problems as well).

##### How do we find out that our docs have drifted from the API?

The way we answered this question before was to go through the spec and make
sure that the happy path at least is correctly documented, i.e., that a
generated python client using Yelp's
[`bravado`](https://github.com/Yelp/bravado) library can interact with the API
without errors. It was a manual process that relied heavily on our python
client repository. A different strategy we could consider would be to generate
a scala client using the hosted version of a spec on Swaggerhub and ensure that
we can drop in the data model in the generated client in place of the existing
data model. Testing this would require investing some software development time
in tooling. Another option is to rely on upcoming
[`panrec`](https://github.com/jisantuc/panrec) features to parse the generated
client's datamodel and the existing datamodel to ensure that they agree.

Both of these strategies will ensure only that the data models are correct
without detecting, e.g., whether we've moved a route. That's a consistency
check beyond what we've done before, but it still leaves a lot of room for us
not to get the spec exactly right in a way that makes us spend potential
support time (triaging issues, responding to help requests) on spec maintenance.

##### How can we document different versions of the API at the same time?

The only strategy I've come up with for the manual maintenance version is a lot
of copying and pasting. Supposing some route exists `/v1/models` and another
route exists `/v2/models`, I don't know how to use OpenAPI to share things
between those two endpoints. Later changes, like adding a new response type to
both, I think would need to be manually written into both places. This sounds
like a headache.

## `tapir`

Changes to generate docs with `tapir` are
[here](https://github.com/jisantuc/scala-api-doc/compare/master..feature/js/tapir-auto-doc).
Docs are served on `localhost:8080/api/hello/docs.yaml` (you can
put that directly into swagger editor).

`tapir` is a library for separating the description of APIs from their
implementation and interpreting those descriptions into different outputs. For
example, an endpoint description can be interpreted into
[documentation](https://github.com/jisantuc/scala-api-doc/blob/feature/js/tapir-auto-doc/app-backend/api/src/main/scala/com/jisantuc/apidoc/HelloService.scala#L52)
(a YAML string) or into
[a server](https://github.com/jisantuc/scala-api-doc/blob/feature/js/tapir-auto-doc/app-backend/api/src/main/scala/com/jisantuc/apidoc/HelloService.scala#L49-L51),
given a function that maps the inputs described in the endpoint into the
outputs described in the endpoint.

`Endpoint`s in `tapir` explicitly encode input types, output types, and errors.
An `Endpoint[I, E, O, S]` maps inputs of of type `I` to outputs of type `O`,
returning errors of type `E`, in streams of type `S`. So far I have not needed
the stream type for anything. `tapir` makes it easy to add inputs to an
endpoint (chain `.in` calls on the endpoint), to add outputs (`.out`), and to
add metadata (`.name` and `.description`).

The worst thing that happened to me while using `tapir` was that I accidentally
wound up with unreachable routes. It seems like `tapir`'s http4s interface
wants us not to mount services onto paths (e.g. `Router("/v1" -> new V1API, "/v2" -> new V2API)`),
but instead to include all path components in the endpoint descriptions.

I tested out serving the docs with an algebraic data type and adding an
authenticated route to make sure that I understood how both of those paths
work. Both were straightforward and the ADT response was correctly encoded as a
`oneOf`. While the default response from a `Left` in my authentication function
was a 400 instead of a 401, that's primarily a consequence of my extremely
simplified endpoints that don't know how to encode specific errors, so can't do
anything to
[discriminate the response to return](https://tapir-scala.readthedocs.io/en/latest/endpoint/statuscodes.html#dynamic-status-codes).

`tapir` endpoints can also be interpreted as clients, but I did not test this
feature.

##### How do we find out that our docs have drifted from the API?

Our docs cannot drift from the API, because the docs and the server are
interpretations of the same endpoints.

##### How can we document different versions of the API at the same time?

I think we can do this by separating endpoint components. The
[authentication docs](https://tapir-scala.readthedocs.io/en/latest/endpoint/auth.html#authentication)
mention defining the `auth` input first, so that it can be shared by many
endpoints, and I believe we could do something similar with version inputs,
e.g.,

```scala
object Endpoints {
  val v1 = endpoint.in("/v1")
  val v2 = endpoint.in("/v2")
  val scenesEndpointV1 = v1.in("/scenes")...
  val scenesEndpointV2 = v2.in("/scenes")...
}
```

Then each versioned collection of endpoints could be served off of its version
prefix.

## `rho`

Changes to generate docs with `rho` are
[here](https://github.com/jisantuc/scala-api-doc/compare/master..feature/js/rho-auto-doc).
Docs are served on `localhost:8080/api/hello/swagger.json` (you can
put that directly into swagger editor).

`rho` is a library in the http4s ecosystem for automatically generating Swagger
documentation with an alternative routing DSL. Route and parameter descriptions
are combined with the routing logic to create `RhoRoutes[F]`, which can be
transformed into normal `HttpRoutes[F]` with a `RhoMiddleware` that also serves
the API documentation as `json` on a configurable endpoint.

The worst part about `rho` is having to keep a number of odd operators in your
head. For example, capturing query parameters is `>>>`, specifying response
types is `^`, adding descriptions is `**`, and binding the route to a function
for business logic is `|>>`. It's possible these are something we'd get used to
over time, but I had to look each of them up again to write what they were.

`rho` generates Swagger (OpenAPI 2.0) specifications as json. Because of this,
it does not have access to the `oneOf` keyword for describing responses that
might have one of several different schemas. The generated json included one
error, which was that the `Json` schema (generated from an endpoint returning
`circe`'s `Json` type) was missing but referred to in a route.

##### How do we find out that our docs have drifted from the API?

Our docs cannot drift from the API, because the `RhoMiddleware` creates docs
for what our routes are actually doing.

##### How can we document different versions of the API at the same time?

Each service can serve its own docs, so mounting a service in the http4s
`Router` will also mount documentation for that service.

## `guardrail`

`guardrail` http4s support is [not currently
documented](https://guardrail.dev/scala/http4s/), so I did not investigate this
library further.

# Decision

We should use `tapir` for automatically generating API documentation. The ADT
support and straightforward API (inputs use `.in`, outputs use `.out`, auth
extractors use `auth`) will flatten out the learning curve, and we'll have a
stable and correct reference point for API documentation that users setting up
their own deployments can refer to. We can call this out at the beginning of
the README and hopefully save ourselves from having to answer an entire
category of questions.

# Consequences

- The first routes added to the API will be slightly more difficult, because
  they'll include writing API routes with a new library for the first time.
- The README should be updated to point to the location of the API
  documentation.
