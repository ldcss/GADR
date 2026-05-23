# ADR 0004: direnv for nix editor integration

Date: 2018-09-30

## Status

Accepted

## Context

As per [ADR-0003](adr-0003-nix-for-dependency-management.md) we are using nix to manage our
dependencies.

Good nix development involves switching into a `nix-shell` which contains the appropriate libraries
*and* binaries required to build your program. This is handy in a terminal but is tricky for an
editor as editors often require access to the same binaries to enable fancy features like
auto-completion and jump-to-function.

Currently I'm using emacs. I _could_ open emacs from within a `nix-shell` but I want to be able
to switch between buffers from other projects without breaking everything.

One option which I've used in the past is to leverage [direnv](https://github.com/direnv/direnv).

Direnv is a tool that can modify your environment variables on a per-directory basis. Crucially it supports nix and has an emacs plugin. We just need to create an `.envrc` containing `use nix`.

Another option is to leverage [nix-buffer](https://github.com/shlevy/nix-buffer) which seems
to require the creation of a `.dir-locals.el`. This approach seems promising but I haven't
been able to make sense of the fairly sparse documentation and as a result I'll be discarding
this option for now.

## Decision

I will use direnv to integrate editors with nix

## Consequences

- We need to make an `.envrc` file to make everything work
- Only editors with direnv support will be able to take advantage of this change
