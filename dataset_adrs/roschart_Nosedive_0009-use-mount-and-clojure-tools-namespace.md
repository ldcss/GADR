# 9.  Use mount and clojure tools namespace
Date: 2018-06-19

## Status
Accepted

## Context
In clojure a normal work flow is use the repl. The problem is that when you reload the appliction the states die.

[mount](https://github.com/tolitius/mount) is here to preserve all the Clojure superpowers (powerful, simple and fun) while making the application state enjoyably reloadable.

Depending on how application state is managed during development, the above three superpowers can either stay, go somewhat, or go completely.
## Decision
Use mount libray and clojure tools space.

The decision of mount over component is made afer review bouth solutions. My feeling is
 * Mount is more clojure dialect oriented
 * Mount use namespace and component
 Records, this made that the compliler control the dependencies
 * Mount is [less contagious](https://engineering.riotgames.com/news/taxonomy-tech-debt)   

## Consequences
 * We need change the project.clj, and start to define some states 

