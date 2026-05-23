# Language choice
## Added at: 2019-12-28 22:51:57 UTC
## Status: Accepted

## Context
Currently I'm capable of using two languages to develop what I'm intending to do - Ruby and Javascript. It didn't make sense to use both, since functionality is not that big. The main thing I wanted to check was related to presentation layer, so it kinda limited my options as well.

## Decision
Use Javascript to develop proof of concept.

## Consequences
### Positive
* Fast time of development.
### Negative

## Other options
* Javascript + Ruby - Javascript would need to be used for rendering table of contents anyway, but rendering itself could also be done in Ruby with `erb` templates instead of `ejs`. I abandoned this choice though due higher use of Javascript on daily basis in recent time.
