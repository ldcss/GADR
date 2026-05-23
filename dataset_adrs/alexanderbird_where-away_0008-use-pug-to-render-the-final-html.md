# 8. use pug to render the final html

Date: 2020-11-09

## Status

Accepted

Extends [3. output a single html file](0003-output-a-single-html-file.md)

## Context

We'll need to combine html, js, and css. The ways I've done this before are:
- all in one file
  - this is gross, hard to write, and nigh impossible to unit test
- bash & sed to replace placeholders blocks with file content
  - this is cheap, but gross, and can cause trouble with character escaping.
    It's effectively a polyglot and forces you to think about bash when writing
    JavaScript or CSS. Painful
- webpack with inlining plugins
  - it's possible to use webpack to produce a single standalon html file
    including css and javascript, but it takes a lot of configuration &
    fiddling. I've done it, it was super powerful, but took an afternoon to set
    up.
      - fiddling with plugins
      - different plugins for CSS and JavaScript
      - it felt like webpack was not the right tool
- use a template engine like Pug that supports inlining JavaScript out of the
  box
    - if necessary, this can be coupled with webpack or equivalent -- use a JS
      tool to combine the JavaScript; use Pug to pull the built JavaScript into
      the final HTML

## Decision

Use Pug to produce the HTML from a template.

## Consequences

It is tempting to make pug a runtime dependency, but I'd like to avoid
unnecessary runtime dependencies. Instead, use `pug.compile` to create a template
at build time. We can accept the user input as parameters and hydrate the
template with them at runtime.
