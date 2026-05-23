# 8. Migrate away from MDX

Date: 2022-01-15

## Status

Accepted

## Context

MDX—while great—has some notable tradeoffs that have made writing quickly more difficult for me.

- MDX files are not portable outside of React(ish) runtimes.
- MDX requires a "runtime" of accepted components. It does not gracefully degrade to raw HTML if those components are not provided.
- The type of content I produce on my blog does not require high interactivity or customization. MDX feels like overkill right now.
- MDX actually serves as a distraction while writing at the moment. I feel like constraints are more helpful ("is this a `<Callout>` or a `blockquote`?" decision fatigue).
- Other authoring tools (i.e. Notion, Bear, etc) usually allow exporting something as markdown, but if MDX is a first-class citizen on the blog this means there's an extra conversion step to get unified design.

## Decision

Remove all MDX files in favor of simple Markdown

## Consequences

- Richly interactive articles/examples will become harder. This may require reevaluating this decision in the future if such articles become common.
- I'll be limited to GitHub-flavored markdown or raw markdown in the articles I write.
- I may need to introduce some shortcodes for custom interactivity.
