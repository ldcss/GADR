# Use Go As Server Language

The EASi developers need a language
to support the application server side.

## Considered Alternatives

* Go
* Language with widespread web framework
  (ex. Ruby or Python)
* JavaScript/Node

## Decision Outcome

* Chosen Alternative: *Go*

The top reason for selecting Go are
that the team has in house expertise.
The application team is immediately ready
to produce client value in Go
due to their familiarity with the language and ecosystem.

It is also a modern strong typed language,
which provides compile time safety,
as opposed to common web app alternatives,
such as Ruby, Python, or JavaScript.

The benefits of using languages
with more mature web frameworks
(such as Rails or Django),
are outweighed by the flexibility
of using a frontend framework driven UI
with a JSON API for data retrieval.
For the latter,
Go provides excellent tooling
in its standard libraries and ecosystem,
for building mature, stable, maintainable APIs.

## Pros and Cons of the Alternatives

### Go

* `+` Familiarity with team.
* `+` Common tools across Truss projects.
* `+` Static typed.
* `-` Relatively immature compared to Ruby/Python
  in web app ecosystem.

### Language with Widespread Web Framework (Ruby or Python)

* `+` Easy to bootstrap common application features.
* `+` Strong, mature ecosystem and community.
* `-` Dynamically typed
* `-` Not in application team's toolset.

### JavaScript with Node

* `+` Frontend/Server in same language.
* `+` Single package system (NPM or yarn)
* `-` Dynamically typed.
* `-` Not in application team's toolset,
  especially for server side applications.
