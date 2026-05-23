# Configure Rspec with Files

## Context

As part of the template there is a need to provide a base configuration for Rspec. Ideally this would be performed using the `rails generate rspec:install` command. However, on testing the Thor command `generate("rspec:install)"` it froze when it got to install rspec. This is likely due to [spring running as described in this error](https://stackoverflow.com/questions/33189016/how-to-solve-rails-generate-commands-hanging).

For now, `hmu-rails` just uses template files to configure rspec. An option to explore in the future would be to test whether calling `spring stop` as part of a `generate_rspec` method would resolve this issue.

## Decision

For now `hmu-rails` will use template files for configuring rspec for speed but revisit the need to run the install command in the future.

## Status

Accepted

## Consequences

**Positive**

Unblocks this issue and it works for now. We can be more specific about the configuration of rspec, which is kind of the point.

**Negative**

If rspec-rails generate script changes, we won't be able to take advantage of these.
