# 3. hapijs-server

Date: 2019-05-10

## Status

2019-05-10 proposed

2019-05-10 accepted

## Context

[ExpressJS][1] is the default server for most NodeJS projects. However I have found that it does not include the features that I would prefer -

- Robust and extensible architecture to decompose a project
- Handle common use cases like file uploads
- Nice error handling e.g. 404, route collisions
- Easy to test server behaviour including middleware

[HapiJS][2] has the above features and

- All essential dependencies are maintained by the same team
- Accessible and friendly community

[Read more][3] about HapiJS

## Decision

In the context of a fullstack NodeJS project and facing the concern of making better architecture decisions, I decided to use HapiJS to achieve better quality measured by test coverage and composable architecture. I accept that I will have to rely on documentation and source code more since HapiJS is not as well written about because of its lower popularity.

## Consequences

- Use HapiJS

[1]: https://expressjs.com/
[2]: https://hapijs.com
[3]: https://hueniverse.com/why-you-should-consider-hapi-6163689bd7c2
