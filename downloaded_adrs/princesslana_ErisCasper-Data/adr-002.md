# ADR 2: Code Generation Process

## Context

We will be generating a number of classes as per [ADR 1](adr-001.md).

Generated classes should be generated during the build process and not committed to GitHub.
This ensures we have reproducable builds and makes it clear that generated classes are not to be edited manually.

We wish to publish artifats to the central maven repository.
This does not necessarily limit us to working with Maven, but it encourages us to stick it.

Using a compiled language to run the code generation would require two passes of compilation
(or another/project module) - one to compile the codegen scripts, another to run it.

## Decision

We will use ruby to write the code generation scripts.

We will run them using the [jruby-maven-plugins](https://github.com/torquebox/jruby-maven-plugins) as part of the
`generate-sources` phase of the
[maven lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)

## Consequences

Maven is maintained as the build tool.
This means that the current process of publishing artifacts remains unchanged.

Code generation is scripted.
This avoids two passes of compilation.

The choice of scripting language is due to the existing knowledge of Ruby and jruby-maven-plugins from
[Princess Lana](https://github.com/ianagbip1oti).
It was known that it was possible to perform this with Ruby, so no investigation was done into whether
Python, Javascript, or other might have been possible.



