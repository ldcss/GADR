# 4. Use vim-plug in favour of Vundle

Date: 2021-01-18

## Status

Accepted

## Context

Vundle hasn't been updated for a while (Aug 2019 at time of writing) and I'd
read a bit about how vim-plug was pretty good. And it felt like it was time for
a change.

## Decision

[vim-plug](https://github.com/junegunn/vim-plug) will be used to manage Vim
plugins in favour of [Vundle](https://github.com/VundleVim/Vundle.vim).

## Consequences

There should be no negative consequences from the change other than the small
amount of time it takes to install the plugins with vim-plug.
One change that might be worth remembering is that vim-plug stores plugins in
`~/.vim/plugged/` rather than `~/.vim/bundle`.
