# 9. Use preact

Date: 2022-01-18

## Status

Superceded by [13. Migrate to SvelteKit](0013-migrate-to-sveltekit.md)

## Context

Since this app doesn't rely heavily on React libraries or things like suspense, switching to [`preact`](https://preactjs.com/) offers a significantly smaller bundle size (~70kb => ~40kb).

Due to preact's compatability package very little should change in day-to-day development.

## Decision

Use `preact` instead of `react`.

## Consequences

- Using libraries becomes a little more difficult, if the React library doesn't work with the compatability layer.
- Bundle size should decrease, and performance should increase 🏎
- Might make migrating to a different React meta-framework more difficult (i.e. Remix), if Preact isn't supported. However, might not as long as the compat layer still works.
