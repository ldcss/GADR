# 5. Replace redirects with HTML pages

Date: 2021-02-25

## Status

Accepted

Amends [4. Client-side routing using history API and redirects](0004-client-side-routing-using-history-api-and-redirects.md)

## Context

As described in [ADR #4. Client-side routing using history API and redirects](0004-client-side-routing-using-history-api-and-redirects.md), on deploy we generate a HTML file for each pixel art entry which contains the following:

- A title
- Additional meta tags to generate a link preview via [Open Graph Protocol](https://ogp.me/)
- Some JavaScript to redirect back to `index.html` where users will see the actual pixel art gallery

This allows us to link to a specific entry and have preview images for each entry. However, this approach also leads to a somewhat slower page load when the user visits one of these links as the browser will land on one page, execute some JavaScript, and then load another page before they can see the actual pixel art gallery.

## Decision

We will modify the existing process of generating pages for each pixel art entry to render a HTML page with the relevant `meta` tags and, rather than redirecting users to the main page, will instead load the same JavaScript loaded by `index.html`

## Consequences

- Users will now have mostly the same experience when viewing the gallery either by visiting `index.html` directly or by visiting any of the pages for a specific piece.
