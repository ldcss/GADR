# 15. Migrate to sveltekit...again

Date: 2022-11-23

## Status

Accepted

Supercedes [13. Migrate to SvelteKit](0013-migrate-to-sveltekit.md)

Supercedes [14. migrate to Remix](0014-migrate-to-remix.md)

## Context

So...SvelteKit made a [_major_ change](https://github.com/sveltejs/kit/discussions/5748) to their data fetching and routing recently, and ✨ I love it. ✨

I tried the new version of SvelteKit out with some other side projects and have found the new setup to be super productive. Since data loading was one of my main gripes with SvelteKit when I migrated away from it to Remix, I figured it was time to revisit the decision.

So here's a few of the items around the context to migrate the website _back_ to SvelteKit.

1. **Static rendering is supported.** While I understand the stance of the Remix folks about static rendering being more-or-less the same as caching, it's easy and simple for me to statically render all my posts. I like the "hybrid" approach that frameworks like SvelteKit and Next.js offer.
2. **Genuinely welcoming community.** I'm not gonna say too much on this, but I found the Svelte community to be much more welcoming in all channels (discord, twitter, etc). A lot less throwing punches at the broader web community and a lot more shipping amazing code.
3. **Dead simple.** SvelteKit (after the big routing change) is simpler than all the alternatives.
4. **Sooooo productive.** I found myself forgetting about all the framework-specific parts and just building my pages. It just feels soooooo natural.
5. **Potentally "a next big thing".** Of course, this is a bet, and a potentially risky one. But I use React at work, so it's not like my React skills are atrophying. Svelte is poised to take some large chunks of the web app scene once SvelteKit hits a stable `1.0` version.

## Decision

Rewrite portfolio using SvelteKit

## Consequences

- Data fetching is still super simple
- Less confusion about what code runs on server and what runs on client.
- Get to satisfy itch for "shiny new tools" 😜
