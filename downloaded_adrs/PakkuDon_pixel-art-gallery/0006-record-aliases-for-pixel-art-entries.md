# 6. Record aliases for pixel art entries

Date: 2021-05-24

## Status

Accepted

## Context

Currently we use an image's filename as a URL slug so that we can link to individual pixel art entries.

Occasionally we may want to change these filenames as there may be a typo in the name, or we may decide that we want to change our naming convention. As these URLs may have been bookmarked or shared elsewhere we still want the old URLs to remain valid.

## Decision

Pixel art entries may define multiple aliases. These can be thought of as previous filenames (sans file extension).

When we generate pages for each pixel art entry we will also generate a page for each alias listed which will include the same link preview but redirect to the canonical URL instead.

## Consequences

- Previous URLs for pixel art entries will remain valid.
  - We can still invalidate old URLs by _not_ defining them in an entry's list of aliases.
- As the redirects generated for aliases will use the same mechanism outlined in [4. Client-side routing using history API and redirects](./0004-client-side-routing-using-history-api-and-redirects.md) these redirects will have a longer load time.
