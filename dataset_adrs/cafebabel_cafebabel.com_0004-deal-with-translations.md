# 4. Deal with translations

Date: 2017-11-13

## Status

Accepted


## Context

Articles can be translated in English, French, Spanish, Italian and
German.

Original articles are not necessarily in English and initial text of a
given translation can be itself an already translated article.

Each translation must keep a link to the original article.

The review process remains the same with a draft status.

The translated article must both have a redactor and a translator.


## Decision

A new MongoDB document will be created for each translation.

That document will inherit from the Article model.


## Consequences

A link must be present from a translation to its source article.

A translator must be set for a given translation.

It will be easy to perform a query to retrieve all translations in a
given language.
