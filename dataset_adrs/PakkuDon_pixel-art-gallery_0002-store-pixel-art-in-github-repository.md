# 2. Store pixel art in Github repository

Date: 2020-11-06

## Status

Accepted

## Context

I've recently gotten into pixel art. I wanted a place to host these so I could share them later if I felt so inclined. But I didn't want to create a new account or use an existing account that had any PII associated with it.

I also figured I could make another side project out of this.

## Decision

- Pixel art will be stored in a git repository that will be hosted on Github.
- Link to image and associated details will be stored in a text file so they can be displayed in a UI later.

## Consequences

- Images and their associated metadata will be stored under version control so that they can be revised or reverted with relative ease.
- As new images will be added in git commits my Github contribution graph may still appear green even if I haven't coded at all.
