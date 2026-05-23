# 5. Using markdown in Jekyll.

Date: 2017-06-08

## Status

Accepted

## Context

Jekyll supports the markdown syntax by default. Files must be prefixed 
with a YAML Front Matter section for the engine to categorize, format 
and display the blog post/page. Project documentation files (e.g.: `README.md`) 
taken from a project release bundle must not have YAML Front Matter section 
or any Jekyll or third-party specific formatting but pure markdown syntax.

## Decision

Create YAML Front Matter index files in the `/_posts` directory, 
like `2017-01-01-readme.md` and use the `include_relative` 
[Jekyll command](https://jekyllrb.com/docs/includes/) to include 
the unmodified `README.md`. Create a new layout format in Jekyll 
named `markdown.html` and use the `markdown` value specifying 
the `layout:` in the YAML Front Matter index file, see example:

```
2017-01-01-readme.md

---
layout: markdown
title: Sample title here
weight: 3
category: a-category-here
categoryItemType: documentation
categoryItemIsShown: 0
---
{% include_relative README.md  %}
```

The `markdown.html` should have the same contents as the `post.html` 
with an extra `article`, `section` tags surrounding the `{content}` tag
to keep formatting consistent.

## Consequences

Original project documentation files e.g.: `README.md` does not have 
to be modified, they can be copied from a project bundle into Jekyll easily.
Layout for the `README.md` must be specified in the index file 
e.g.: `2017-01-01-readme.md`. Layout/formatting of the display blog post/page
can be changed/updated without the need of modifying any project documentation. 
`README.md` files can reside anywhere in Jekyll project structure 
if using the `include_relative` command to include them.
