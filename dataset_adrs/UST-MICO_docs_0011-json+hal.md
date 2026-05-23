# JSON+hal as serialization Format for the API

## Context and Problem Statement

The backend needs to serialize the REST resources before sending them via http to the client.

## Decision Drivers

- the format should be REST/[HATEOAS](https://spring.io/understanding/HATEOAS) compatible (e.g. allow hyperlinks)
- the format should be easy to parse/serialize for the backend and the client

## Considered Options

- xml
- pure json
- [json+hal](http://stateless.co/hal_specification.html)

## Decision Outcome

We will use json+hal (or the spring implementation for json with hyperlinks) without the [`_embedded`](https://tools.ietf.org/html/draft-kelly-json-hal-08#section-4.1.2) attribute (because of its complexity to implement correctly).

```eval_rst
.. seealso::

   * :doc:`0010-rest-api-design`
   * `Richardson Maturity Model <https://martinfowler.com/articles/richardsonMaturityModel.html>`_
   * `HATEOAS is for Humans <http://intercoolerjs.org/2016/05/08/hatoeas-is-for-humans.html>`_
```
