# Follow Conventional Commits

## Status

Accepted

## Context

The point of the tool is to enforce good commit hygiene, which is easy to compromise while trying to just get good code out. We should pick a standard that seems like it's popular or otherwise conventional, and not overly strict for flexibility.

## Decision

Use [Conventional Commits v1.0.0-beta.4]. It's similar enough to [Semantic Commits] and its inspiration [Angular Commits], but loose enough and working on being an independent standard.

## Consequences

* Commits take more work; breaking changes would require a commit body, for example.
* It's easier to map bumps in versions.
* Some tools that do this, or something similar to this, require node.js installed and / or a node.js project with which it could work. In choosing this standard, we're in theory choosing to add new flexibility.

<!-- References -->
[Semantic Commits]: https://seesparkbox.com/foundry/semantic_commit_messages
[Angular Commits]: https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit
[Conventional Commits v1.0.0-beta.4]: https://www.conventionalcommits.org/en/v1.0.0-beta.4/