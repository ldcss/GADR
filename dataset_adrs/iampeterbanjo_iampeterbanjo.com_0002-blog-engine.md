# 2. blog-engine

Date: 2019-05-10

## Status

2019-05-10 proposed

2019-05-10 accepted

## Context

I wanted to create a website blog using [Markdown][1], a [static site generator][2] and [HapiJS][3] to serve the files. Static site generators I tried, in order, were -

### [11ty][4]

Pros

- Easy setup
- Predictable static file output
- Relatively small codebase
- Supporst different template engines

Cons

- The frontmatter parser [didn't work as I expected][7]
- Template errors were not reported and would only fail on build
- Needs some attention to make production ready e.g. SEO, images, favicons etc

### [Gatsby][5]

Pros

- Modern [JAMstack][8] project with React
- Batteries included by default - includes helpers for favicons, image loading, SEO etc.
- Opportunity to use GraphQL

Cons

- Doesn't output static files - [totally depends on clientside JavaScript][9]
- It relies on service workers to cache responses which causes flakey e2e tests and unpredictable behaviour
- Developing static files based on API was difficult because of caching and unexpected error handling
- Relatively complex project with separate build, develop steps, config, plugins etc

### [Hugo][6]

Pros

- Fast and mature static site generator
- Small footprint

Cons

- Written in Go - I prefer fullstack JavaScript for this site

## Decision

In the context of using several static site generators each of them had with their own downsides. And facing the concern of having blog that I can easily maintain and customise I decided to build my blog with HapiJS to achieve a smaller blog footprint, predictable behaviour and an opportunity to learn something new. I accept that I'm re-inventing the wheel.

## Consequences

- More work - I have to learn how to do that
- One single server running during development
- I can make all decisions for creating, parsing and serving content
- Can be error prone

[1]: https://daringfireball.net/projects/markdown/
[2]: https://www.staticgen.com/
[3]: https://hapijs.com
[4]: https://11ty.io
[5]: https://gatsbyjs.org
[6]: https://gohugo.io
[7]: https://github.com/11ty/eleventy/issues/415
[8]: https://jamstack.org/
[9]: https://github.com/gatsbyjs/gatsby/issues/962
