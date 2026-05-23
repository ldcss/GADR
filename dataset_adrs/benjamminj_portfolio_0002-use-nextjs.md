# 2. Use NextJS

Date: 2020-09-03

## Status

Superceded by [14. Migrate to SvelteKit](0014-migrate-to-sveltekit.md)

Superceded by [13. Migrate to SvelteKit](0013-migrate-to-sveltekit.md)

## Context

There's a few large architectural decisions that were made before I started using ADRs, so I'm backfilling them a little.

[NextJS](https://nextjs.org/) is a fantastic framework for building scalable, enterprise-grade applications with React.

NextJS has a few notable contrasts to [Gatsby](https://www.gatsbyjs.com/) (which this blog was previously built on) which factored into the decision to use it here. Some of these are captured below, some of my thoughts can be found in [this article by Jared Palmer](https://jaredpalmer.com/gatsby-vs-nextjs).

Here's some loose bullet points behind my reasoning behind using NextJS for this site.

- NextJS comes baked in with routing, webpack configurations, TypeScript support, and a whole host of other things. Less fiddling with tools, more writing meaningful code.
- In general, Gatsby is more "plugin-oriented", NextJS is more "recipe-oriented". While plugins are nice to get a ton of functionality, each plugin introduces another dependency that you have to maintain, upgrade. Each new dependency introduces another point of failure.
- NextJS doesn't have a GraphQL layer baked into it. For a website of this size I felt like being required to use the GraphQL layer to access markdown files was overkill.
- NextJS allows you to build "hybrid" applications—ones where there's a combination of server-rendered (SSR) pages, static-rendered pages, and prerendered pages. There's not likely to be any SSR pages in this website, but NextJS sets you up for flexibility as time goes on in regards to rendering strategies.
- NextJS is a super in-demand, "hot" skill in the React community, so having my website built on top of it both keeps me fresh on the latest patterns and showcases my abilities.
- I like working with NextJS! I like the framework and how they've chosen the APIs!

## Decision

I will use [NextJS](https://nextjs.org/) as the framework on top of React to build this website

## Consequences

This will influence some of the patterns throughout the application. Stuff like routing, file structure, etc.
