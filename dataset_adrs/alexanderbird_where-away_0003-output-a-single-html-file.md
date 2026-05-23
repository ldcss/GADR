# 3. output a single html file

Date: 2020-11-06

## Status

Accepted

Extended By [8. use pug to render the final html](0008-use-pug-to-render-the-final-html.md)

## Context

### Things we don't need

1. It's not going to be a very fancy site
2. It's not going to be very big
3. It's not going to be very customizable
4. It's not important to be able to embed this in another site

### Things we do need

1. really simple interface
2. really simple to deploy
3. I'd like to be able to re-use this in new contexts easily
  - that means I'll have forgotten how to use it and will need to re-learn
    quickly

## Decision

Output a single HTML file with embedded JavaScript and CSS.

## Consequences

### Build

```bash
npx where-to > bookmarks.html < bookmarks.json
```

### Deployment options:
  - file:// link to a location on disk
  - static website hosting
  - document management tool that renders HTML documents (or returns it with the
    right doctype header so your browser renders it)
  - etc.?

