# 2. Use Google Closure Compiler

Date: 2021-02-08

## Status

Accepted

Explains [3. Test Distributed Files Only](0003-test-distributed-files-only.md)

## Context

We must allow developers to use new JavaScript syntax and features without excluding older execution environments. Code must be automatically checked against common development mistakes and optimised for download and execution.

## Decision

We acknowledge that there is a plethora of Node.js tooling options available, however we have decided to use the [Google Closure Compiler]. It is developed and maintained by Google and is used for high traffic, complex and global applications such as Gmail and Google Maps. By adopting this tool we leverage decade of research and engineering in that field.

## Consequences

- Code can be written using modern JavaScript to improve the development experience.
- Code can be compiled to ES5 to maximise reach.
- Code can be minified and optimised.
- Longer compiling and testing cycles.
- Simpler [software composition analysis][what-is-sca].

[Google Closure Compiler]: https://github.com/google/closure-compiler
[what-is-sca]: https://snyk.io/blog/what-is-software-composition-analysis-sca-and-does-my-company-need-it/
