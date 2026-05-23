# 2. Use toml for config file

Date: 2020-07-05

## Status

Accepted

## Context

`stentor` needs to pick a config file format.
The options under consideration are yaml and toml.

Both options are human readable and writable,
allow for easy parsing of structured data,
and are supported by well maintained libraries.

yaml has the benefit of being more straightforward to write,
especially for nested structures.
However, toml is intended for config files,
and provides stricter parsing out of the box.

## Decision

`stentor` will use toml for its config file.

## Consequences

toml provides a strict parser that will return errors on unrecognized fields.
This makes validation easier and allows `stentor` to provide hints to users to correct typos.
The downside is that toml's syntax for arrays of tables is more complicated than yaml,
and is easier to write incorrectly.
This is mitigated for `stentor`'s use case,
because the only array of tables needed is for customizing the sections.
