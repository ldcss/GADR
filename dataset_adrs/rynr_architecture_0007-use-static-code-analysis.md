# 7. Use static code analysis

Date: 2018-07-06

## Status

Accepted

Is related to [2. Apply clean code guidelines](0002-apply-clean-code-guidelines.md)

## Context

You never think of everything. Sticking to standards is a very good
thing to prevent you from doing things that can go bad. Those also
helps making the code be more readable and structured.

## Decision

Use Static Code Analysis to find violations of standards.

## Consequences

For java it's a good idea to use [sonar](https://www.sonarsource.com/),
for JavaScript, there is [sonar](https://www.sonarsource.com/) as well,
and [ESLint](http://eslint.org/), [JSHint](http://jshint.com/) or
[JSLint](http://jslint.com/). For other languages, check this
[List of tools for static code analysis](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis).

Have the build failing, when there are violations.
