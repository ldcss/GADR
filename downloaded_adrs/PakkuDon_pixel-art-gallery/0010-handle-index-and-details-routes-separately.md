# 10. Handle index and details routes separately

Date: 2023-09-09

## Status

Accepted

## Context

Currently the index route (`/`) and details route (`/:id`) are both rendered using a dynamic route with optional catch-all segments (`/src/app/[[...id]]/page.tsx`).

Both routes share similar behaviour:

- `/` route displays details for the latest entry posted
- `/:id` route displays details for the entry specified in the URL (either by ID or alias)

This approach has a few issues:

- The `id` parameter is either undefined or an array. The use of a singular noun with an array type can be confusing, but the singular noun `id` makes sense as this route will only contain zero or one segments.
- The dynamic route with optional catch-all needs to handle four potential cases. Each case only matters to one specific type of route:
  1. Case where there is no id present (index route)
  2. Case where ID is present and matches an entry (details route)
  3. Case where ID is an alias for an entry (details route)
  4. Case where ID is present but does not match any existing entries (details route)
- At the time of writing an [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image) file cannot be specified for the details route. This prevents us from co-locating the code used to generate preview images with the page the preview image is for. (Source: [Github issue: [NEXT-1204] opengraph-image can't be used to accept params in catch-all routes (Error: Catch-all must be the last part of the URL.)](https://github.com/vercel/next.js/issues/49630))

## Decision

The dynamic route `[[...id]]` will be re-implemented as two separate routes

- `/page.tsx` will handle the index route
- `/[id]/page.tsx` will handle the details route

## Consequences

- Details routes can specify a preview image using an [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image) file.
  - **Note:** At the time of writing Open Graph images cannot be statically generated for dynamic routes. (Source: [Github issue: OpenGraph images are not statically generated for dynamic routes](https://github.com/vercel/next.js/issues/51147))
- There may be lag when navigating between the `/` and `/:id` routes as both routes will be code-split.
