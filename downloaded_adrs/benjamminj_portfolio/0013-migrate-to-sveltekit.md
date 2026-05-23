# 13. Migrate to SvelteKit

Date: 2022-05-02

## Status

Supercedes [2. Use NextJS](0002-use-nextjs.md)
Supercedes [11. Use Preact](0011-use-preact.md)
Superceded by [14. Migrate to Remix](0014-migrate-to-remix.md)

Superceded by [15. Migrate to sveltekit...again](0015-migrate-to-sveltekit-again.md)

## Context

One driving principle behind my website is "this is my corner of the internet". As such, I don't need to provide too much context behind a rewrite beyond "I want to try {insert tool or technique} out"

That said, there's a few motivations for wanting to use Svelte / SvelteKit:

1. It's fun. I've been having much more fun developing with SvelteKit than with Next.js lately.
2. Tiny JS bundles. Granted, I had already decreased the bundle size by [using Preact](0011-use-preact.md) but Svelte can support an even smaller bundle due to how the compiler optimizes the client-side JS.
3. Leans in to the way the web works. This is a big thing for me right now, that you wanna "lean in" to whatever platform you've chosen. SvelteKit really has progressive enhancement at the core of many decisions, which I like.
4. Learn a new skill. I'm already proficient in React, and use it in my day job. So I'm not too worried about getting stale skills there.
5. Built-in animations. Need I say more?!?

## Approach

I'm not gonna do "the big rewrite" (like when I rewrote this website from Gatsby) this time, I wanna incrementally move over for a couple reasons:

1. This is how you do it "in the real world". Companies rarely have the ability to hit pause on product development and just rewrite their app. But you also don't get to do a lot of incremental rewrites over the course of a career (esp. not from one framework to another) — it's a risky move for a business, potentially sinking hundreds of thousands of dollars.
2. This allows me to profile pages side-by-side when I port them to SvelteKit.

And here's _how_ I plan to do it:

- Set up endpoints on the SvelteKit app that proxy the Next.js application (similar to Next.js `rewrites`). Update the "main" `benjaminjohnsonme` app to deploy the _SvelteKit_ app and deploy the Next.js app on a separate server.
- Migrate pages "as-is" to SvelteKit, with no design changes.
- Once all pages have been rewritten, there should be nothing left in the Next.js application.
- Finally, remove the Next.js codebase and move the SvelteKit subdirectory to be at the top-level.

This approach has a number of benefits over a full rewrite:

- Preserves git history (sort of). While the components and routes won't be the same file, stuff like `package.json`, `adr`, and `content` doesn't have to get changed.
- Keeps scope small for me. Esp. important right now on my schedule.
- Closer to what you'd do in the real world.

## Decision

Migrate to SvelteKit incrementally.

## Consequences

- CI may take longer while the rewrite is in progress, since I'll be deploying _both_ apps
- CI may also get more difficult, esp. testing the preview applications. I'll need to check how I can get the e2e tests to run (may need to write my own script, which could also be fun).
- Animations should get easier since they're built-in with Svelte. 😍
- Complex CSS selectors will become SO MUCH EASIER since Svelte allows you to just write regular ol' CSS (and can still use Tailwind w/ `@apply`).
