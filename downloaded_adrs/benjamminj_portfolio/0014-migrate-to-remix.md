# 14. migrate to Remix

Date: 2022-05-28

## Status

Supercedes [14. Migrate to SvelteKit](0014-migrate-to-sveltekit)

Superceded by [15. Migrate to sveltekit...again](0015-migrate-to-sveltekit-again.md)

## Context

After a small amount of experimentation, SvelteKit was not getting the perf gains that I wanted to see. A large amount of this was that I wanted more granular control over _how_ data is fetched and JS loaded.

Secondly, I felt like SvelteKit just wasn't the right fit for me at this point in time. Not because it's bleeding edge (I like that) and I really like the idea of it being a compiler, IDK. Just too many quirks, esp with the data loading.

In contrast, [Remix](https://remix.run/) is super simple and super powerful. I feel like I want to keep exploring Remix's ideas and it continues to give me enough to be creative. So perfect for my website, especially as I start to think about making it more dynamic (content on GitHub, or in a DB, etc.)

## Decision

Migrate away from NextJS and SvelteKit to Remix.

## Consequences

- Data fetching becomes easier and significantly less convoluted
- Static rendering becomes "impossible". Right now I'm just pre-building all of my posts during build and importing them into the lambda as a JS object. This will only scale to a certain point, but I think it'll be decently far in the future.
