# 7. Use a single Docker container for dummies, docker-compose for more complex projects

Date: 2018-02-15

## Status

Accepted

## Context

Dummy services such as api-dummy are stateless, do not require many components such as databases and caches, and do not produce logs.

The ease with of pushing, pulling and running a single image inside larger orchestration is its selling point.

Real projects have dependencies that should be centralized to specialized containers such as `nginx` or `postgres`. These dependencies are not maintained in-house. These dependencies also have to be bootstrapped in a certain order.

Real projects also have various volumes that need to be mounted for them to function, such as configuration files.

`docker-compose` has some support for IDEs, and is portable between laptops and headless environments such as `ci` and `prod`.

## Decision

By default, use a single docker image to ship dummy projects. Provide additional options for setup if needed to satisfy other requirements.

Use one or more `docker-compose.yml` files to build and deploy real projects.

## Consequences

Every dummy project should be set up by simply running:

```
docker run [-p 8080:80] elifesciences/*_dummy
```

although it can have multiple variants of its image that cater to more complex and/or optimized setups.

Real projects should be set up by running:

```
docker-compose build
docker-compose up
```
