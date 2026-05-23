# Keep Server and Frontend in Same Repository

Since server and frontend development will be split up
with different technologies,
we have the option of also splitting up their code repositories.

## Considered Alternatives

* Server and frontend in one repo
* Server and frontend in separate repos

## Decision Outcome

* *Server and frontend in one repo*

Having a single entry point for code,
documentation,
and build/CLI tools
gives us low overhead for bootstrapping the application
and developer onboarding.
This outweighs the need for separate
development and deployment flows.
We don't anticipate a heavy decoupling of
the frontend and server in this application.
In the case where they need to be packaged separately as services,
we can split out directories into separate repositories.

## Pros and Cons of the Alternatives

### Server and frontend in one repo

* `+` One developer environment to set up.
* `+` All components are easily searchable
  either via GitHub repository or `git grep`.
* `+` One set of command line and deployment tools.
* `+` No cross repo versioning or submodules.
* `+` Changes requiring frontend and server work
  are easily viewable.
* `-` Harder to track server and frontend development separately.
* `-` Harder to package/provision individual components.
* `-` Multiple languages/package systems means root directory bloat.

### Server and frontend in separate repos

* `+` Development can happen in separate workflows
  and history of each stack can be viewed independently.
* `+` Deployments can happen in separate workflows.
* `+` Single language/stack setup per repository.
* `-` Overhead of orchestration between repositories.
* `-` No single view of application code.
