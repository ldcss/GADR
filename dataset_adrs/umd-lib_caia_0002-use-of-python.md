# 0002 - Use of Python

Date: May 11, 2020

## Context

An application has to written in some programming languge.

## Decision

The following languages were considered for this application:

* Java
* Python
* Ruby

The initial inclination was to use either Java or Ruby, based solely on
developer experience.

After discussions with Ben Wallberg, it was decided to use Python because:

* The application is fairly simple, an unlikely to reach a complexity where
  Java's more explicit typing and compile-time verification is needed.
* We have a number of developers familiar with Python, providing a broader
  base from which to draw support.
* While we are content with using Ruby (specifically Ruby on Rails) for website
  projects, this is a command-line application. We have fewer developers
  familiar with Ruby.

## Consequences

Choosing a programming language is obviously foundational to a project.
Fortunately, this project is straightforward enough that it could be
implemented fairly easily in any modern programming language.
