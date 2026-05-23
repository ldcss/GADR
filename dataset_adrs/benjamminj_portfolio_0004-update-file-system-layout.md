# 4. Update file-system layout

Date: 2020-09-14

## Status

Accepted

## Context

Right now the file system is getting a little messy. In the spirit of "code gardening" and cleaning as you go, I think it's now time to do some dedicated shuffling of files.

The `src` folder was nice for a while but I think it's a remnant from the days when this site was on Gatsby. I think it just adds an extra level of file system that might not be needed.

Historically, I've seen that companies rarely make the mistake of having too flat of a file structure. It's usually that folders are too nested.

The goal of this is to experiment with a very _flat_ file structure and see how well it scales to more complex use cases.

## Decision

The filesystem will be updated to look like the following.

```bash
root/
├─ pages/ # NextJS page components
│   ├─ page.tsx
├─ lib/ # helper functions, utilities
│   ├─ utility.ts
│   ├─ utility.test.ts
├─ styles/ # CSS-in-JS helpers
├─ components/ # reusable building blocks
│   ├─ Component.tsx
│   ├─ Component.test.tsx
├─ writing/
│   ├─ post-a.mdx
│   ├─ post-b.mdx
├─ images/
│   ├─ image-a.png
├─ tests/ # page-level integration tests
├─ e2e/ # end-to-end tests
├─ package.json, tsconfig.json, etc.
```

## Consequences

- This will better organize things and hopefully make the project a little more approachable.
- A flat file structure might result in things being grouped by _type_ rather than by _domain_.
- Having the test files in the same folder level with the source files might get cluttered.
- This structure might not scale as the website code gets larger. But I think it's appropriate for the current amount of code.
- It might make sense to combine `styles` and `lib` into a single folder. For now I'll keep them separate
